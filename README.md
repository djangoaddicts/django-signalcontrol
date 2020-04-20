# django-signalcontrol
A django extension for dynamically enabling/disabling model-based signals. 

| | |
|--------------|------|
| Author       | David Slusser |
| Description  | A django extension for dynamically enabling/disabling model-based signals. |
| Requirements | `Python 3.x`<br>`Django 2.2.x` |


# Documentation
Full documentation can be found on http://django-signalcontrol.readthedocs.org. 
Documentation source files are available in the docs folder.


# Installation
- pip install django-signalcontrol
- add signalcontrol to your INSTALLED_APPS
- run migrations python ./manage.py migrate signalcontrol


# Features

### signal decorator


### admin interface



# Usage Example

.. code-block:: python

@receiver(post_save, sender=MyCoolModel)
@signal_control
def msg_my_model_two(sender, instance, created, **kwargs):
    """ some signal """
    print("you just saved an instance of MyCoolModel")

..