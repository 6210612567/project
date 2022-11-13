from django.urls import path, include
from . import views

# from . import views_fronts
app_name = 'web'


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("pdpa_page", views.pdpa_page, name="pdpa_page"),
    # path("register", views_fronts.register, name="register"),
    # path("test", views_fronts.test, name="test"),

    # path('api/v1/', include(front_urls)),
]
