from django.db.models.signals import (post_save, pre_init, post_init, pre_save, pre_delete, post_delete,
                                      m2m_changed, pre_migrate, post_migrate)

# import models
from .models import (SignalControl)


def signal_control(func):
    """ decorator used on signals to check if a model signal should be executed """

    def func_wrapper(*args, **kwargs):
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
        model_name = kwargs['instance']._meta.model_name

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
        signal_control = SignalControl.objects.get_or_create(**lookup_data, defaults=default_data)[0]

        # enable/disable signal
        if signal_control.enabled == False:
            return None
        else:
            return func(*args, **kwargs)

    return func_wrapper
