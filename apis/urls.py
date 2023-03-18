from django.urls import path, include
from .views import AuthenticationApiView
from .views import StudentDataApiView
# from .views import MajorApiView
from .views import StudentDepartmentApiView
from .views import InstructorDepartmentApiView
from .views import InstructorApiView
# from .views import ReportStdGenderApiView
# from .views import ReportStdAdyearApiView
# from .views import TestApiView

app_name = 'apis'

report_std_urls = (
    [
        # path('gender/', ReportStdGenderApiView.as_view()),
        # path('adyear/', ReportStdAdyearApiView.as_view()),
        
    ],
    'report_std')



v1_urls = (
    [
        path('authentication/', AuthenticationApiView.as_view()),
        ####### Student API
        path('stu/student', StudentDataApiView.as_view()),
        path('stu/department', StudentDepartmentApiView.as_view()),
        ####### Student Report API
        # path('report/std/', include(report_std_urls)),
        ####### Instuctor API
        path('ins/instructor', InstructorApiView.as_view()),
        path('ins/department', InstructorDepartmentApiView.as_view()),

        
    ],
    'v1')





urlpatterns = [
    path('v1/', include(v1_urls)),

    # path('api/v1/', include(front_urls)),
]
