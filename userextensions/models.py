"""

"""
from django.db import models
from django.contrib.auth.models import User
from djangohelpers.managers import HandyHelperModelManager


class UserExtensionBaseModel(models.Model):
    """ base model for UserExtension tables """
    objects = HandyHelperModelManager()
    created_at = models.DateTimeField(auto_now_add=True, help_text="date/time when this row was first created")
    updated_at = models.DateTimeField(auto_now=True, help_text="date/time this row was last updated")

    class Meta:
        abstract = True


class Theme(UserExtensionBaseModel):
    """ table to track front-end themes """
    name = models.CharField(max_length=32, unique=True, help_text="name of theme")
    css_file = models.CharField(max_length=32, unique=True, blank=True, null=True,
                                help_text="path to css file for theme")

    def __str__(self):
        return self.name


class UserPreference(UserExtensionBaseModel):
    """ table to track user preferences """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='preference')
    theme = models.ForeignKey(Theme, blank=True, null=True, help_text="theme to use for web pages",
                              on_delete=models.CASCADE)
    recents_count = models.IntegerField(default=25, blank=True, null=True,
                                        help_text="number of recents to keep a record of")
    page_refresh_time = models.IntegerField(default=5, blank=True, null=True,
                                            help_text="time, in minutes, to auto-refresh a page (where applicable")

    def __str__(self):
        return self.user.username


class UserRecent(UserExtensionBaseModel):
    """ table to track user's recently visited urls """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recent')
    url = models.URLField(help_text="url endpoint")

    class Meta:
        unique_together = (('url', 'user'), )

    def __str__(self):
        return self.url


class UserFavorite(UserExtensionBaseModel):
    """ table to track user's favorite urls """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite')
    name = models.CharField(max_length=32, blank=True, null=True, help_text="name/label/reference for this favorite")
    url = models.URLField(help_text="url endpoint")

    class Meta:
        unique_together = (('url', 'user'), )

    def __str__(self):
        return self.url
