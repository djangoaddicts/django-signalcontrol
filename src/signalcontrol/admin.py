from django.contrib import admin

# import models
from .models import SignalControl


def enable(modeladmin, request, queryset):
    for item in queryset:
        item.enabled = True
        item.save()


def disable(modeladmin, request, queryset):
    for item in queryset:
        item.enabled = False
        item.save()


enable.short_description = 'enable signal'
disable.short_description = 'disable signal'


class SignalControlAdmin(admin.ModelAdmin):
    list_display = ['signal_name', 'signal_type', 'model_name', 'app_name', 'enabled']
    search_fields = ['app_name', 'model_name', 'signal_name', 'signal_type']
    list_filter = ['app_name', 'model_name', 'signal_name', 'signal_type', 'enabled']
    actions = [enable, disable]


# Register models
admin.site.register(SignalControl, SignalControlAdmin)
