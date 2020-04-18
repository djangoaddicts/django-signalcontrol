from django.contrib import admin

# import models
from .models import (SignalControl)


class SignalControlAdmin(admin.ModelAdmin):
    list_display = ['id', 'app_name', 'model_name', 'signal_name', 'signal_type', 'enabled']
    search_fields = ['app_name', 'model_name', 'signal_name', 'signal_type']
    list_filter = ['app_name', 'model_name', 'signal_name', 'signal_type', 'enabled']


# Register your models here.
admin.site.register(SignalControl, SignalControlAdmin)
