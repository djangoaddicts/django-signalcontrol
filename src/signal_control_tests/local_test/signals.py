from django.db.models.signals import (ModelSignal, post_save, pre_init, post_init, pre_save, pre_delete, post_delete,
                                      m2m_changed, pre_migrate, post_migrate)
from django.dispatch import receiver

try:
    from django.dispatch.dispatcher import WEAKREF_TYPES
except ImportError:
    import weakref
    WEAKREF_TYPES = weakref.ReferenceType,

import inspect
import six
import ctypes
import gc

# import models
from .models import (SignalControl, MyModelOne, MyModelTwo, MyModelThree)


def signal_control(func):

    def func_wrapper(*args, **kwargs):
        SIGNAL_NAMES = {
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
        # print('model name: ', model_name)

        # get app name
        app_name = kwargs['instance']._meta.model._meta.app_label
        # print('app name: ', app_name)

        # get signal name
        signal_name = func.__name__
        # print('func :', signal_name)

        # get signal type
        signal = kwargs['signal']
        signal_type_name = SIGNAL_NAMES.get(signal, 'unknown')
        # print('signal type: ', signal_type_name)

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


@receiver(post_save, sender=MyModelOne)
@signal_control
def msg_my_model_one(sender, instance, created, **kwargs):
    """  """
    print("you just saved an instance of MyModelOne")


@receiver(post_save, sender=MyModelTwo)
@signal_control
def msg_my_model_two(sender, instance, created, **kwargs):
    """  """
    print("you just saved an instance of MyModelTwo")


@receiver(post_save, sender=MyModelThree)
@signal_control
def msg_my_model_three(sender, instance, created, **kwargs):
    """  """
    print("you just saved an instance of MyModelThree")
