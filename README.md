# django-signalcontrol
A django extension for dynamically enabling/disabling signals. This application allows django signals to be disabled or enabled on-demand through the django admin interface. 


| | |
|--------------|------|
| Author       | David Slusser |
| Description  | A django extension for dynamically enabling/disabling signals. |
| Requirements | `Python 3.x`<br>`Django>=2.2.x` |


# Documentation
Full documentation can be found on http://django-signalcontrol.readthedocs.org. 
Documentation source files are available in the docs folder.


# Installation
- pip install django-signalcontrol
- add signalcontrol to your INSTALLED_APPS
- run migrations python ./manage.py migrate signalcontrol


# Features

### signal decorator
SignalControl can be added to a signal with the provided decorator. In the signals.py file, import the signalcontrol
decorator and add the signal_control decorator to the line directly above the signal definition. Example:


### admin interface
An django admin interface for django-signalcontrol is available to set signals to enabled or disabled. This displays
all signals that can be controlled, and lists the application, model, signal receiver and signal name.
Additionally, full search is available and filters are available for each field.
Signals can be enabled or disabled individually or in bulk.


# Usage Example

```python
    from signalcontrol.decorators import signal_control

    @receiver(post_save, sender=MyCoolModel)
    @signal_control
    def msg_after_my_model_save(sender, instance, created, **kwargs):
        """ some signal """
        print('you just saved an instance of MyCoolModel')
```

