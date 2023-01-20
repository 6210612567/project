from django.urls import path, include
from . import views

# from . import views_fronts
app_name = 'web'


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("pdpa_page", views.pdpa_page, name="pdpa_page"),
    path("setting", views.setting_page, name="setting_page"),
    path("privacy", views.privacy_page, name="privacy_page"),
    path("home", views.home, name="home"),
    path("channel", views.channel_page, name="channel_page"),
    path("Document", views.document, name="document"),
    path("Report", views.report_page, name="report_page"),
    path("Helpdesk", views.help_page, name="help_page"),
    path("update", views.update_page, name="update_page"),
    path("Authkey", views.createChannel_page, name="createChannel_page"),
    path("DocumentsGettingStart", views.getStart_page,
         name="getStart_page"),
    path("DocumentsTwoFactor", views.twoFactor_page,
         name="twoFactor_page"),
    path("insert_channel", views.insert_channel_view, name="insert_channel_view"),
    path("edit_channel", views.edit_channel_view, name="edit_channel_view"),
    path("delete_channel/<str:channel_id>", views.delete_channel_view, name="delete_channel"),
    path("activate_2fac", views.activate_2fac_view, name="activate_2fac"),
    path("delete_2fac", views.delete_2fac_view, name="delete_2fac"),

    path("test/<int:pin>", views.test_page, name="test_page"),
]
