django-userprofile
===============
A user extension module for django. This includes some basic uer profile settings and 
tracking of a users favorites and recently visited urls within the project. 


Documentation
-------------
Full documentation can be found on http://django-userextensions.readthedocs.org. 
Documentation source files are available in the docs folder.


Installation 
------------
- pip install django-userextensions
- add django-userextensions to your INSTALLED_APPS
- to include recents tracing, add 'userextensions.middleware.UserRecentsMiddleware' to your middleware
- to include views to manage favorites and recents, in the project-level urls.py file add the following to your urls.py:
    from userextensions.urls import *
    path('', include('userextensions.urls'), ), 
- run migrations python ./manage.py migrate userextensions


License
-------
django-userextensions is licensed under the MIT license (see the LICENSE file for details).
