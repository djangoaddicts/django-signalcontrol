.. _installation:


Installation
============

The django-userextensions package is available on Python Package Index (PyPI) and can be installed via pip with the
following command:

.. code-block:: console

    pip install django-userextensions
..


Adding django-userextensions to your django project
---------------------------------------------------

To use django-userextensions in your project, add 'userextensions' to INSTALLED_APPS in your settings.py file and run
``manage.py migrate`` to create the required database structure.

.. code-block:: python

    INSTALLED_APPS = [
        ...
       'userextensions',
    ]
..


Optional Feature Configurations
-------------------------------

To include recents tracking, add 'userextensions.middleware.UserRecentsMiddleware' to your middleware.

.. code-block:: python

    MIDDLEWARE = [
        ...
        'userextensions.middleware.UserRecentsMiddleware',
    ]
..

By default, some fixed URLs and URLs with specific prefixes are excluded from being stored in recents. These can be
modified by setting the ``SKIP_URL_PREFIX_LIST`` and ``SKIP_FIXED_URL_LIST`` parameters in the settings.py file. URLs
stored in recents can also be filtered by http request methods. By default only ``GET`` is enabled. This can be modified
by changing the ``TRACK_METHOD_LIST`` parameter in the settings.py file.

.. code-block:: python

    SKIP_URL_PREFIX_LIST = ['/admin/', '/__debug__/', ]
    SKIP_FIXED_URL_LIST = ['/', '/login/', '/logout/', ]
    TRACK_METHOD_LIST = ['GET', ]
..

Several views, with applicable templates, are provided for use. Note, action-based views, such as ``RefreshApiToken``
and ``UserLoginRedirect`` do not require templates. Views with GUIs, such as list and detail pages, include templates
with requirements including Twitter Bootstrap. An included base template will be used for these views. You can override
this by setting the ``BASE_TEMPLATE`` parameter to your preferred base template in the settings.py file.

To use these, set the ``BASE_TEMPLATE`` parameter in the settings.py file and include the userextensions.urls your
project-level urls.py file.

.. code-block:: python

    from userextensions.urls import *

    urlpatterns = [
        ...
        path('', include('userextensions.urls'), ),
    ]
..

.. code-block:: python

    BASE_TEMPLATE = 'location_of_your_base_template'
..

To allow the custom user start page, update the ``LOGIN_REDIRECT_URL`` parameter in your settings.py file to point to
the userextensions user_login_redirect view. Optionally, the ``LOGIN_REDIRECT_URL_DEFAULT`` parameter can be set to
define the page redirected to when a user does not have a start page configured.

.. code-block:: python

    LOGIN_REDIRECT_URL = '/userextensions/user_login_redirect'
    LOGIN_REDIRECT_URL_DEFAULT = 'myapp/some_cool_page'
..
