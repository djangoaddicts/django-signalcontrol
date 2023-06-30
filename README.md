# django-signalcontrol
[![Downloads](https://static.pepy.tech/badge/django-signalcontrol)](https://pepy.tech/project/django-signalcontrol)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7516/badge)](https://bestpractices.coreinfrastructure.org/projects/7516)

![PyPI - Python](https://img.shields.io/pypi/pyversions/django-signalcontrol)
![PyPI - Django](https://img.shields.io/pypi/djversions/django-signalcontrol)

Django signalcontrol is a django extension for dynamically enabling/disabling signals. This application allows django signals to be disabled or enabled on-demand through the django admin interface. 

<br/>

## Code Quality
| Workflow | Description             | Status                                                                       |
|----------|-------------------------|------------------------------------------------------------------------------|
|Bandit|security checks|![Bandit](https://github.com/djangoaddicts/django-signalcontrol/actions/workflows/bandit.yaml/badge.svg)|
|Black|code formatting|![Black](https://github.com/djangoaddicts/django-signalcontrol/actions/workflows/black.yaml/badge.svg)|
|CodeQL|security analysis|[![CodeQL](https://github.com/djangoaddicts/django-signalcontrol/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/djangoaddicts/django-signalcontrol/actions/workflows/github-code-scanning/codeql)|
|Coveralls|code coverage status|[![Coverage Status](https://coveralls.io/repos/github/djangoaddicts/django-signalcontrol/badge.svg)](https://coveralls.io/github/djangoaddicts/django-signalcontrol)|
|Isort|python import ordering|![Isort](https://github.com/djangoaddicts/django-signalcontrol/actions/workflows/isort.yaml/badge.svg)|
|Mypy|static type checking|![Mypy](https://github.com/djangoaddicts/django-signalcontrol/actions/workflows/mypy.yaml/badge.svg)|
|Pytest|unit testing|![Pytest](https://github.com/djangoaddicts/django-signalcontrol/actions/workflows/pytest.yaml/badge.svg)|
|Radon|code complexity analysis|![Radon](https://github.com/djangoaddicts/django-signalcontrol/actions/workflows/radon.yaml/badge.svg)|
|Ruff|static code analysis|![Ruff](https://github.com/djangoaddicts/django-signalcontrol/actions/workflows/ruff.yaml/badge.svg)|
|Safety|dependency scanner|![Saftey](https://github.com/djangoaddicts/django-signalcontrol/actions/workflows/safety.yaml/badge.svg)|

<br/>

### Code Coverage Dashboard:
https://coveralls.io/github/djangoaddicts/django-signalcontrol

<br/>

## Documentation
Full documentation can be found on http://django-signalcontrol.readthedocs.org. 
Documentation source files are available in the docs folder.

<br/>

## License
django-signalcontrol is licensed under the GNU-3 license (see the LICENSE file for details).

https://github.com/djangoaddicts/django-signalcontrol/blob/docs/LICENSE 

<br/>

## Installation
- install via pip:
    ``` 
    pip install django-signalcontrol
    ```
- add the following to your INSTALLED_APPS in settings.py:

    ```python 
    djangoaddicts.signalcontrol
    ```

<br/>

## Features
### Signal Decorator
SignalControl can be added to a signal with the provided decorator. In the signals.py file, import the signalcontrol
decorator and add the signal_control decorator to the line directly above the signal definition. 


### Admin Interface
An django admin interface for django-signalcontrol is available to set signals to enabled or disabled. This displays
all signals that can be controlled, and lists the application, model, signal receiver and signal name.
Additionally, full search is available and filters are available for each field.
Signals can be enabled or disabled individually or in bulk.

<br/>

## Usage Example

```python
from signalcontrol.decorators import signal_control

@receiver(post_save, sender=MyCoolModel)
@signal_control
def msg_after_my_model_save(sender, instance, created, **kwargs):
    """ some signal """
    print('you just saved an instance of MyCoolModel')
```
