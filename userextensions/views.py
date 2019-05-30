"""

"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.views.generic import View, DeleteView
from rest_framework.authtoken.models import Token
from braces.views import LoginRequiredMixin

# import models
from userextensions.models import (UserRecent, UserFavorite)


class RefreshApiToken(LoginRequiredMixin, View):
    """ delete current user token and create a new one """
    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            Token.objects.get_or_create(user=request.user)
        except Exception as err:
            messages.add_message(request, messages.ERROR, "Could not complete requested action: {}".format(err),
                                 extra_tags='alert-danger')
        return redirect(self.request.META.get('HTTP_REFERER'))


class AddFavorite(LoginRequiredMixin, View):
    """ add (the current) url to the list of user favorites """
    def post(self, request):
        referrer = self.request.META.get('HTTP_REFERER')
        name = self.request.POST.dict().get('name', None)

        # do not track url if user is not authenticated or user can not be determined
        if not request.user.is_authenticated:
            return redirect(referrer)
        user = getattr(request, 'user')
        if not user:
            return redirect(referrer)

        try:
            recent, is_new = UserFavorite.objects.get_or_create(url=referrer,
                                                                user=request.user,
                                                                defaults=dict(url=referrer,
                                                                              user=request.user,
                                                                              name=name,
                                                                              updated_at=timezone.now())
                                                                )
            if is_new:
                messages.add_message(request, messages.INFO, "Successfully added favorite",
                                     extra_tags='alert-info')
            else:
                messages.add_message(request, messages.INFO, "This url is already in your favorites",
                                     extra_tags='alert-info')
        except Exception as err:
            messages.add_message(request, messages.ERROR, "Error adding favorite: {}".format(err),
                                 extra_tags='alert-danger')
        return redirect(referrer)


class DeleteFavorite(LoginRequiredMixin, DeleteView):
    """ delete a favorite (by pk) and return to the referring page """
    def delete(self, request, *args, **kwargs):
        UserFavorite.objects.filter(**kwargs).delete()
        messages.add_message(self.request, messages.INFO, "Favorite successfully deleted", extra_tags='alert-info')
        return redirect(self.request.META.get('HTTP_REFERER'))


class DeleteRecent(LoginRequiredMixin, DeleteView):
    """ delete a recent (by pk) and return to the referring page """
    def delete(self, request, *args, **kwargs):
        UserRecent.objects.filter(**kwargs).delete()
        messages.add_message(self.request, messages.INFO, "Recent successfully deleted", extra_tags='alert-info')
        return redirect(self.request.META.get('HTTP_REFERER'))
