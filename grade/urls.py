from django.urls import path, include
from . import views

# from . import views_fronts
app_name = 'grade'


urlpatterns = [
    path("", views.index, name="index"),

]
