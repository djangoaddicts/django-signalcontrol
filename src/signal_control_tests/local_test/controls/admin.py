from django.contrib import admin

# import models
from .models import (SignalControl, MyModelOne, MyModelTwo, MyModelThree)


def enable(modeladmin, request, queryset):
    for item in queryset:
        item.enabled = True
        item.save()


enable.short_description = 'enable signal'


def disable(modeladmin, request, queryset):
    for item in queryset:
        item.enabled = False
        item.save()


disable.short_description = 'disable signal'


class SignalControlAdmin(admin.ModelAdmin):
    list_display = ['signal_name', 'signal_type', 'model_name', 'app_name', 'enabled']
    search_fields = ['app_name', 'model_name', 'signal_name', 'signal_type']
    list_filter = ['app_name', 'model_name', 'signal_name', 'signal_type', 'enabled']
    actions = [enable, disable]


# Register your models here.
admin.site.register(SignalControl, SignalControlAdmin)
admin.site.register(MyModelOne)
admin.site.register(MyModelTwo)
admin.site.register(MyModelThree)
