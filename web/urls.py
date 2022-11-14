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
    # path("register", views_fronts.register, name="register"),
    # path("test", views_fronts.test, name="test"),

    # path('api/v1/', include(front_urls)),
]
