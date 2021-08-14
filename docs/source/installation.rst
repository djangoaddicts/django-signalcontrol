.. _installation:


Installation
============

The django-signalcontrol package is available on Python Package Index (PyPI) and can be installed via pip with the
following command:

.. code-block:: console

    pip install django-signalcontrol
..


Adding django-signalcontrol to your django project
---------------------------------------------------

To use django-signalcontrol in your project, add 'signalcontrol' to INSTALLED_APPS in your settings.py file and run
``manage.py migrate signalcontrol`` to create the required database structure.

.. code-block:: python

    INSTALLED_APPS = [
        ...
       'signalcontrol',
    ]
..


Enabling signal control on a model signal
-----------------------------------------
SignalControl can be added to a model signal via a provided decorator. In the signal.py file, import the signalcontrol
decorator and add the signal_control decorator to the line directly above the signal definition. Example:

.. code-block:: python

    from signalcontrol.decorators import signal_control

    @receiver(post_save, sender=MyCoolModel)
    @signal_control
    def msg_after_my_model_save(sender, instance, created, **kwargs):
        """ some signal """
        print('you just saved an instance of MyCoolModel')
..
