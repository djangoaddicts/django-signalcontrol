"""

"""
from django.utils import timezone
from django.conf import settings
from django.urls import resolve
from urllib.parse import urlparse

# Use MiddlewareMixin when present (Django >= 1.10)
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

# import models
from userextensions.models import UserRecent


class UserRecentsMiddleware(MiddlewareMixin):
    """ add url to user recents on page request """

    def process_request(self, request):
        """ read uers and url (path) from request, if valid and not in a skip list, add to user's recents """
        # only track specified methods
        track_method_list = getattr(settings, 'TRACK_METHOD_LIST', ['GET'])
        if request.method not in track_method_list:
            return

        # do not track url if user is not authenticated
        if not request.user.is_authenticated:
            return
        if not getattr(request, 'user'):
            return

        # do not track if url (full path) can not be determined
        path = getattr(request, 'get_full_path')()
        if not path:
            return

        # do not track admin or debug urls
        skip_url_prefix_list = getattr(settings, 'SKIP_URL_PREFIX_LIST', ['/admin/', '/__debug__/'])
        for prefix in skip_url_prefix_list:
            if path.startswith(prefix):
                return

        # do not track urls in the skip_fixed_url_list
        skip_fixed_url_list = getattr(settings, 'SKIP_FIXED_URL_LIST', ['/', '/login/', '/logout/', ])
        for url in skip_fixed_url_list:
            if path == url:
                return

        # do not track invalid urls
        try:
            resolve(urlparse(path).path)
        except:
            return

        # add recent
        UserRecent.objects.update_or_create(url=request.get_full_path(),
                                            user=request.user,
                                            defaults=dict(url=request.get_full_path(),
                                                          user=request.user,
                                                          updated_at=timezone.now())
                                            )
