from django.urls import path, include
from .views import AuthenticationApiView
from .views import StudentDataApiView
from .views import MajorApiView
from .views import DepartmentApiView
from .views import InstructorApiView
# from .views import TestApiView

app_name = 'apis'
v1_urls = (
    [
        path('authentication/', AuthenticationApiView.as_view()),
        path('student', StudentDataApiView.as_view()),
        path('major', MajorApiView.as_view()),
        path('department', DepartmentApiView.as_view()),
        path('instructor', InstructorApiView.as_view()),
        # path('test', TestApiView.as_view()),
    ],
    'v1')



urlpatterns = [
    path('v1/', include(v1_urls)),

    # path('api/v1/', include(front_urls)),
]
