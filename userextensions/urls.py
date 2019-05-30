from django.urls import path
from userextensions.views import (AddFavorite, DeleteFavorite, DeleteRecent, RefreshApiToken)


app_name = "userextensions"

urlpatterns = [
    # create views
    path('add_favorite/', AddFavorite.as_view(), name='add_favorite'),

    # delete views
    path('delete_favorite/<int:pk>', DeleteFavorite.as_view(), name='delete_favorite'),
    path('delete_recent/<int:pk>', DeleteRecent.as_view(), name='delete_recent'),

    # custom views
    path('refresh_api_token', RefreshApiToken.as_view(), name='refresh_api_token'),

]
