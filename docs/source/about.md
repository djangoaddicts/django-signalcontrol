# About

django-signalcontrol is a reusable django application that adds dynamic control to signals.

With signal_control added to a signal, the signal can by enabled (default) or disabled from the django admin. An entry for the signal is added to the SignalControl table that includes a boolean field to enable/disable the signal. When a signal is disabled it will not execute when dispatched through the receiver, such as post_save.

<br/>

## Requirements & Dependencies

django-signalcontrol is built on Python 3.10.x and Django 4.2.x. For a full list of packages and requirements, please
see the install_requires in the pyproject.toml file.

<br/>
