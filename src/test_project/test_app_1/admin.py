from django.contrib import admin

# import models
from test_app_1.models import (MyModelOne, MyModelTwo, MyModelThree)


class MyModelOneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_filter = []


class MyModelTwoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_filter = []


class MyModelThreeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_filter = []


# register models
admin.site.register(MyModelOne, MyModelOneAdmin)
admin.site.register(MyModelTwo, MyModelTwoAdmin)
admin.site.register(MyModelThree, MyModelThreeAdmin)
