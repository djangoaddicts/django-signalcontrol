Installation
============

django-userextensions can be installed via pip:

.. code-block:: console

    pip install django-userextensions



Add userextensions to INSTALLED_APPS in settings.py file.

.. code-block:: python

    INSTALLED_APPS = [
        ...
       'userextensions',
    ]


To include recents tracking, add 'userextensions.middleware.UserRecentsMiddleware' to your middleware.

.. code-block:: python

    MIDDLEWARE = [
        ...
        'userextensions.middleware.UserRecentsMiddleware',
    ]


By default, some fixed URLs and URLs with specific prefixes are excluded from being stored in recents. These can be modified by setting the SKIP_URL_PREFIX_LIST and SKIP_FIXED_URL_LIST parameters in the settings.py file.

.. code-block:: python

    SKIP_URL_PREFIX_LIST = ['/admin/', '/__debug__/']
    SKIP_FIXED_URL_LIST = ['/', '/login/', '/logout/', ]


Several views, with applicable templates, are provided for use. To use these, include the userextensions.urls your project-level urls.py file.

.. code-block:: python

    from userextensions.urls import *

    urlpatterns = [
        ...
        path('', include('userextensions.urls'), ),
    ]
