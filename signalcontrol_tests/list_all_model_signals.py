# coding:utf-8

import os
import sys
import gc
import inspect
import ctypes
from collections import defaultdict
import linecache

from django.core.management.base import BaseCommand
from django.db.models.signals import *
import environ
import django

# setup django
sys.path.append(str(environ.Path(__file__) - 3))
sys.path.append("/app")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings.local")
django.setup()



try:
    from django.dispatch.dispatcher import WEAKREF_TYPES
except ImportError:
    import weakref
    WEAKREF_TYPES = weakref.ReferenceType,


MSG = '{module}.{name} #{line}'

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


class Command(BaseCommand):
    help = 'List all signals by model and signal type'

    def handle(self, *args, **options):
        print('in handle')
        signals = [obj for obj in gc.get_objects() if isinstance(obj, ModelSignal)]
        # models = defaultdict(lambda: defaultdict(list))
        # print('models: ', models)

        for signal in signals:
            signal_name = SIGNAL_NAMES.get(signal, 'unknown')
            print('signal name: ', signal_name)
            print(signal.receivers)
            for receiver in signal.receivers:
                print(receiver)
                lookup, receiver = receiver
                if isinstance(receiver, WEAKREF_TYPES):
                    receiver = receiver()
                if receiver is None:
                    print('no receiver')
                    continue
                print('got receiver')
                receiver_id, sender_id = lookup

                model = ctypes.cast(sender_id, ctypes.py_object).value
                print('TEST: got model: ', model)
                print('file: ', receiver.__name__)
                print('file: ', receiver.__code__.co_filename)
                print('file: ', receiver.__code__.co_firstlineno)
                # models[model][signal_name].append(MSG.format(
                #     name=receiver.func_name,
                #     module=receiver.__module__,
                #     line=inspect.getsourcelines(receiver)[1], path=inspect.getsourcefile(receiver))
                # )

        # print(models.keys())
        # for key in sorted(models.keys()):
        #     print('' + key.__module__ + "." + key.__name__, u"({})".format(key._meta.verbose_name))
        #     for signal_name, lines in models[key].items():
        #         print(" "*4, signal_name)
        #         for line in lines:
        #             print(" "*8, line)



def scan_for_signals_old():
    """ """
    signals_to_add = []


    # first we get all the signals
    signals = [obj for obj in gc.get_objects() if isinstance(obj, ModelSignal)]

    for signal in signals:
        signal_type = SIGNAL_NAMES.get(signal, 'unknown')

        for receiver in signal.receivers:
            lookup, receiver = receiver
            if isinstance(receiver, WEAKREF_TYPES):
                receiver = receiver()
            if receiver is None:
                continue
            receiver_id, sender_id = lookup

            print('TEST: got signal type: ', signal_type)

            model = ctypes.cast(sender_id, ctypes.py_object).value
            print('TEST: got model: ', model)

            app = model._meta.model._meta.app_label
            print('TEST: got app: ', app)

            signal_name = receiver.__name__
            print('TEST: got signal: ', signal_name)

            file_name = receiver.__code__.co_filename
            line_num = receiver.__code__.co_firstlineno
            print("{} {}".format(file_name, line_num))
            # print(linecache.getline(file_name, line_num + 1))

            # check if this signal has signal_control applied
            if '@signal_control' in linecache.getline(file_name, line_num + 1):
                print('signal_control found!')

            else:
                print('no signal control here')
                continue

            # verify signal
            reciever_data = linecache.getline(file_name, line_num)
            signal_data = linecache.getline(file_name, line_num + 2)
            if signal_type in reciever_data and model in reciever_data and signal_name in signal_data:
                    print("{} - {} - {} - {}".format(app, model, signal_type, signal_name))

                # check if this signal has signal_control applied
                # print('file: ', receiver.__name__)
                # print('file: ', receiver.__code__.co_filename)
                # print('file: ', receiver.__code__.co_firstlineno)


def scan_for_signals():
    """
    Look in apps.py for each app in the project and find signals.py or files under a signals directory. Inspect each
    applicable signals files and find instances of '@signal_control' to identify signals with signal_control applied.
    Create an entry in the SignalControl database for each applicable signal found.
    """
    pass



def main():
    """ script entry point """
    scan_for_signals()


if __name__ == "__main__":
    sys.exit(main())
