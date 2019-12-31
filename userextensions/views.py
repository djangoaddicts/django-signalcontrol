"""
shared views to facilitate user preference actions
"""

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from django.views.generic import View, DeleteView, ListView
from rest_framework.authtoken.models import Token
from djangohelpers.views import FilterByQueryParamsMixin
from braces.views import LoginRequiredMixin

# import models
from userextensions.models import (UserRecent, UserFavorite, UserPreference)

# import forms
from userextensions.forms import UserPreferenceForm


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


class UserLoginRedirect(LoginRequiredMixin, View):
    """ Check if a user has a preferred 'start page' to load after login. I so, redirect to that page after login, else
        redirect to the project root page.
        To enable this redirect, set the LOGIN_REDIRECT_URL parameter in the settings.py to
        /userextensions/user_login_redirect and include userextensions.urls in the project level urls.py
    """
    def get(self, request):
        # get the users preferred start page
        try:
            start_page = request.user.preference.start_page
            if start_page:
                return redirect(start_page)
        except Exception as err:
            messages.add_message(request, messages.ERROR, "Error getting start page; redirect to root".format(err),
                                 extra_tags='alert-danger')
            return redirect("/")


class SetStartPage(LoginRequiredMixin, View):
    """ set the current page as the users preferred 'start page' to be redirected to after login """
    def post(self, request):
        referrer = self.request.META.get('HTTP_REFERER')
        try:
            # do not set start page if user is not authenticated or user can not be determined
            if not request.user.is_authenticated:
                return redirect(referrer)

            # set current url as start page
            request.user.preference.start_page = referrer
            request.user.preference.save()
            messages.add_message(request, messages.INFO, "start page updated!", extra_tags='alert-info')
        except Exception as err:
            messages.add_message(request, messages.ERROR, "Error setting start page: {}".format(err),
                                 extra_tags='alert-danger')
        return redirect(referrer)


class ListRecents(LoginRequiredMixin, FilterByQueryParamsMixin, ListView):
    """ display a list of urls the user has recently visited """
    base_template = settings.BASE_TEMPLATE

    def get(self, request, *args, **kwargs):
        context = dict()
        self.queryset = UserRecent.objects.filter(user=request.user).order_by('-updated_at')
        template = "generic/generic_list.html"
        context['queryset'] = self.filter_by_query_params()
        context['title'] = "Recents"
        context['sub_title'] = request.user.username
        context['table'] = "table/table_recents.htm"
        return render(request, template, context=context)


class ListFavorites(LoginRequiredMixin, FilterByQueryParamsMixin, ListView):
    """ display a list of user defined favorites """
    base_template = settings.BASE_TEMPLATE

    def get(self, request, *args, **kwargs):
        context = dict()
        self.queryset = UserFavorite.objects.filter(user=request.user).order_by('-updated_at')
        template = "generic/generic_list.html"
        context['queryset'] = self.filter_by_query_params()
        context['title'] = "Favorites"
        context['sub_title'] = request.user.username
        context['table'] = "table/table_favorites.htm"
        return render(request, template, context=context)


class DetailUser(LoginRequiredMixin, View):
    """ show user profile """
    base_template = settings.BASE_TEMPLATE
    template = "detail/detail_user.html"

    def get(self, request):
        context = dict()
        # include user preference form
        form_data_user_preferences = dict()
        form_data_user_preferences['form'] = UserPreferenceForm(request.POST or None, instance=request.user.preference)
        form_data_user_preferences['action'] = "Update"
        form_data_user_preferences['action_url'] = reverse('userextensions:detail_user')
        form_data_user_preferences['title'] = "<b>Update Preferences: </b><small> {} </small>".format(request.user)
        form_data_user_preferences['modal_name'] = "update_user_preferences"
        context['form_data_user_preferences'] = form_data_user_preferences

        context['user'] = request.user
        context['token'] = str(Token.objects.get_or_create(user=request.user)[0])
        context['groups'] = sorted([i.name for i in request.user.groups.all()])
        context['base_template'] = self.base_template
        return render(request, self.template, context=context)

    def post(self, request):
        redirect_url = request.META.get('HTTP_REFERER')
        form = UserPreferenceForm(request.POST or None, instance=request.user.preference)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.ERROR, "Preferences updated!", extra_tags='alert-info', )
            return redirect(redirect_url)
        else:
            for error in form.errors:
                messages.add_message(request, messages.ERROR, "Input error: {}".format(error),
                                     extra_tags='alert-danger', )
            return self.get(request)
