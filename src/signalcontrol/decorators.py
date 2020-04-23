import linecache
import re
from django.apps import apps
from django.db.utils import OperationalError
from django.db.models.signals import (post_save, pre_init, post_init, pre_save, pre_delete, post_delete,
                                      m2m_changed, pre_migrate, post_migrate)

# import models
from .models import (SignalControl)


def signal_control(func, **kwargs):
    """ decorator used on signals to check if a model signal should be executed """
    signal_name = func.__name__
    file_name = func.__code__.co_filename
    line_num = func.__code__.co_firstlineno
    reciever_data = linecache.getline(file_name, line_num)
    matches = re.match('@receiver\((\S+), sender=(\S+)[,\)]', reciever_data)
    signal_type_name = matches.group(1)
    model_name = matches.group(2)
    model = [i for i in apps.get_models() if i.__name__ == model_name][0]
    app_name = model._meta.model._meta.app_label or None

    # add the signal to SignalControls
    lookup_data = dict(app_name=app_name, model_name=model_name,
                       signal_name=signal_name, signal_type=signal_type_name)
    default_data = dict(app_name=app_name, model_name=model_name,
                        signal_name=signal_name, signal_type=signal_type_name)
    try:
        control_instance, is_new = SignalControl.objects.get_or_create(**lookup_data, defaults=default_data)
        if is_new:
            print('INFO: registering {} in {} with SignalControl'.format(signal_name, app_name))
    except OperationalError:
        'The SignalControl table does not exist yet so signal entries can not be made'
        pass

    def signal_control_wrapper(*args, **kwargs):
        signal_name_dict = {
            pre_init: 'pre_init',
            post_init: 'post_init',
            pre_save: 'pre_save',
            post_save: 'post_save',
            pre_delete: 'pre_delete',
            post_delete: 'post_delete',
            m2m_changed: 'm2m_changed',
            pre_migrate: 'pre_migrate',
            post_migrate: 'post_migrate',
        }

        # get model name
        model_name = kwargs['instance']._meta.model.__name__

        # get app name
        app_name = kwargs['instance']._meta.model._meta.app_label

        # get signal name
        signal_name = func.__name__

        # get signal type
        signal = kwargs['signal']
        signal_type_name = signal_name_dict.get(signal, 'unknown')

        # add entry to signal_control table
        lookup_data = dict(app_name=app_name, model_name=model_name,
                           signal_name=signal_name, signal_type=signal_type_name)
        default_data = dict(app_name=app_name, model_name=model_name,
                            signal_name=signal_name, signal_type=signal_type_name, enabled=True)
        control_instance = SignalControl.objects.get_or_create(**lookup_data, defaults=default_data)[0]

        # enable/disable signal
        if control_instance.enabled == False:
            return None
        else:
            return func(*args, **kwargs)

    return signal_control_wrapper
