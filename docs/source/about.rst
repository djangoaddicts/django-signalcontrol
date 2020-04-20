.. _about:


About
=====
django-signalcontrol is a reusable django application that adds dynamic control to model signals.
With signal_control added to a model signal, an entry for the signal is added to the SignalControl table that includes
a boolean field to enable/disable the signal. An interface in the django admin console is provided to enable or disable
signals individually or in bulk. When a signal is disabled it will not execute when dispatched through the receiver,
such as post_save.

See details on django-extensions features on the :ref:`Features <features>` page



Requirements & Dependencies
---------------------------

django-signalcontrol is built on Python 3.6.x and Django 2.2.x. For a full list of packages and requirements, please
see the requirements.txt file.

https://github.com/davidslusser/django-signalcontrol/blob/master/requirements.txt
