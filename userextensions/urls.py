from django.urls import path
from userextensions import views

app_name = "userextensions"

urlpatterns = [
    # create views
    path('add_favorite/', views.AddFavorite.as_view(), name='add_favorite'),

    # update views
    path('set_start_page/', views.SetStartPage.as_view(), name='set_start_page'),

    # delete views
    path('delete_favorite/<int:pk>', views.DeleteFavorite.as_view(), name='delete_favorite'),
    path('delete_recent/<int:pk>', views.DeleteRecent.as_view(), name='delete_recent'),

    # custom views
    path('refresh_api_token', views.RefreshApiToken.as_view(), name='refresh_api_token'),
    path('user_login_redirect/', views.UserLoginRedirect.as_view(), name='user_login_redirect'),

]
