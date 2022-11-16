from django.urls import path, include
from .views import AuthenticationApiView
from .views import StudentDataApiView

app_name = 'apis'
v1_urls = (
    [
        path('authentication/', AuthenticationApiView.as_view()),
        path('test', StudentDataApiView.as_view()),
    ],
    'v1')



urlpatterns = [
    path('v1/', include(v1_urls)),

    # path('api/v1/', include(front_urls)),
]
