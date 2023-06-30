import linecache
import re
from functools import wraps

from django.apps import apps
from django.conf import settings
from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)
from django.db.models.signals import (
    m2m_changed,
    post_delete,
    post_init,
    post_migrate,
    post_save,
    pre_delete,
    pre_init,
    pre_migrate,
    pre_save,
)
from django.db.utils import OperationalError

# import models
from .models import SignalControl


def find_app_name(file_name, signal_name):
    """
    attempt to determine the django app name based on a file

    Args:
        file_name: full path and name of file
        signal_name: name of signal (function name)

    Returns:
        name of django app or None if app can not be determined
    """
    file_name = file_name.replace("/", ".")
    for app in settings.INSTALLED_APPS:
        if app in file_name:
            return app
    print(f"ERROR: can not apply SignalControl on {signal_name}; app can not be determined")
    return 1


def init_signal_control(func):
    """
    At django startup, scan signals.py file(s) for signals with signal_contol applied. When found, add to the
    signalcontrol table.

    Args:
        func: function signal_control is decorating

    Returns:
        None on success
        1 if error encountered
    """
    _ = SignalControl.objects.none()
    app_name = None
    model_name = None
    signal_type_name = None
    signal_name = func.__name__
    file_name = func.__code__.co_filename
    line_num = func.__code__.co_firstlineno
    reciever_data = linecache.getline(file_name, line_num).strip()

    # check for model signals
    matches = re.match("@receiver\((\S+), sender=(\S+)[,\)]", reciever_data)
    if matches:
        signal_type_name = matches.group(1)
        model_name = matches.group(2)
        model = [i for i in apps.get_models() if i.__name__ == model_name][0]
        app_name = model._meta.model._meta.app_label or None
    else:
        # check for non-model signals
        matches = re.match("@receiver\((\S+)\)", reciever_data)
        if matches:
            signal_type_name = matches.group(1)
            app_name = find_app_name(file_name, signal_name).split(".")[-1]

    # add the signal to SignalControls
    lookup_data = dict(
        app_name=app_name, model_name=model_name, signal_name=signal_name, signal_type=signal_type_name
    )
    default_data = dict(
        app_name=app_name, model_name=model_name, signal_name=signal_name, signal_type=signal_type_name
    )


    try:
        control_instance, is_new = SignalControl.objects.get_or_create(**lookup_data, defaults=default_data)
        if is_new:
            print("INFO: registering {} in {} with SignalControl".format(signal_name, app_name))
    except OperationalError:
        print("The SignalControl table does not exist yet so signal entries can not be made")
        return 1


def signal_control(func):
    """decorator used on signals to check if a model signal should be executed"""
    init_signal_control(func)

    @wraps(func)
    def signal_control_wrapper(*args, **kwargs):
        signal_name_dict = {
            pre_init: "pre_init",
            post_init: "post_init",
            pre_save: "pre_save",
            post_save: "post_save",
            pre_delete: "pre_delete",
            post_delete: "post_delete",
            m2m_changed: "m2m_changed",
            pre_migrate: "pre_migrate",
            post_migrate: "post_migrate",
            user_logged_in: "user_logged_in",
            user_logged_out: "user_logged_out",
            user_login_failed: "user_login_failed",
        }

        # get signal name
        signal_name = func.__name__

        # get model name
        if kwargs.get("instance", None):
            model_name = kwargs["instance"]._meta.model.__name__
        else:
            model_name = None

        # get app name
        if kwargs.get("instance", None):
            app_name = kwargs["instance"]._meta.model._meta.app_label
        else:
            app_name = find_app_name(func.__code__.co_filename, signal_name).split(".")[-1]

        # get signal type
        signal = kwargs["signal"]
        signal_type_name = signal_name_dict.get(signal, "unknown")

        # add entry to signal_control table
        lookup_data = dict(
            app_name=app_name, model_name=model_name, signal_name=signal_name, signal_type=signal_type_name
        )
        default_data = dict(
            app_name=app_name,
            model_name=model_name,
            signal_name=signal_name,
            signal_type=signal_type_name,
            enabled=True,
        )
        control_instance, is_new = SignalControl.objects.get_or_create(**lookup_data, defaults=default_data)

        # enable/disable signal
        if control_instance.enabled is False:
            return None
        else:
            return func(*args, **kwargs)

    return signal_control_wrapper
