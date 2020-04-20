.. _features:


Features
========

This document details the features currently available in django-signalcontrol.



signal_control decorator
------------------------

SignalControl can be added to a model signal via a provided decorator. In the signal.py file, import the signalcontrol
decorator and add to the line directly above the signal definition.

.. code-block:: python

    from signalcontrol.decorators import signal_control

    @receiver(post_save, sender=MyCoolModel)
    @signal_control
    def msg_my_model_two(sender, instance, created, **kwargs):
        """ some signal """
        print("you just saved an instance of MyCoolModel")
..



Admin Interface
---------------

An django admin interface for django-signalcontrol is available to set model signals to enabled or disabled. This
displays all model signals that can be controlled, and lists the application, model, signal receiver and signal name.
Additionally, full search is available and filters are available for each field.
Signals can be enabled or disabled individually or in bulk.
