import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .authentication import ldap3_authen
# from rest_framework import permissions

# from django.contrib.auth.models import User

# Import models
from web.models import major as Major , StudentShowdetail3 , engr_department as Department ,instructor as Instructor ,ChannelForAPI
# Import filter
from .filter import MajorFilter,StudentShowdetail3Filter,DepartmentFilter,InstructorFilter
from datetime import datetime


def check_permission(request):
        try:
            auth_key = request.headers['Application-Key']
            ChannelForAPI.objects.get(auth_key=auth_key,status=True)
            return True
        except:
            return False


def update_api_limit(secretkey,time):
    channel = ChannelForAPI.objects.get(auth_key=secretkey)
    if channel.limit_time != time:
        channel.limit = 3000
        channel.limit_time = time
        channel.save()
    if channel.limit > 0:
        channel.limit -= 1
        channel.save()
        return True
    else:
        return False

class AuthenticationApiView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        response = ldap3_authen(request.data['username'],request.data['password'])
        if response[0] == True:
            return Response({
                'status':True,
                'message':'Authorized',
                'name':response[1]
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status':False,
                'message':'Unauthorized',
                'name':response[1]
                }, status=status.HTTP_401_UNAUTHORIZED)
        

############### NEW FIND STUDENT DATA BY USING DJANGO FILTER ###############
class StudentDataApiView(APIView):
    permission_classes = []
    
    def get(self, request, *args, **kwargs):
        if not check_permission(request):
            return Response({
                "status": False,
                "error": "Authentication failed due to the following reason: invalid token. Confirm that the access token in the authorization header is valid."
            }, status=status.HTTP_401_UNAUTHORIZED)

        if not update_api_limit(request.headers['Application-Key'],datetime.now().hour):
            return Response({
            "status": False,
            "error": "Api request limit"
            }, status=status.HTTP_408_REQUEST_TIMEOUT)

        student_data_all = StudentShowdetail3.objects.all()
        # Get all data by use filter
        students = StudentShowdetail3Filter(request.GET,queryset=student_data_all).qs
        # Extract data to list for response
        student_context_list=[]
        for student in students:
            student_context_list.append(student.context_data)
        return Response({
            "status": True,
            "message": "Success",
            "data": student_context_list
            }, status=status.HTTP_200_OK)


class MajorApiView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        if not check_permission(request):
            return Response({
                "status": False,
                "error": "Authentication failed due to the following reason: invalid token. Confirm that the access token in the authorization header is valid."
            }, status=status.HTTP_401_UNAUTHORIZED)

        if not update_api_limit(request.headers['Application-Key'],datetime.now().hour):
            return Response({
            "status": False,
            "error": "Api request limit"
            }, status=status.HTTP_408_REQUEST_TIMEOUT)

        major_data_all = Major.objects.all()
        # Get all data by use filter
        majors = MajorFilter(request.GET,queryset=major_data_all).qs
        # Extract data to list for response
        major_context_list=[]
        for major in majors:
            major_context_list.append(major.context_data)
        return Response({
            "status": True,
            "message": "Success",
            "data": major_context_list
            }
            
            , status=status.HTTP_200_OK)



class DepartmentApiView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        if not check_permission(request):
            return Response({
                "status": False,
                "error": "Authentication failed due to the following reason: invalid token. Confirm that the access token in the authorization header is valid."
            }, status=status.HTTP_401_UNAUTHORIZED)

        if not update_api_limit(request.headers['Application-Key'],datetime.now().hour):
            return Response({
            "status": False,
            "error": "Api request limit"
            }, status=status.HTTP_408_REQUEST_TIMEOUT)

        department_data_all = Department.objects.all()
        # Get all data by use filter
        departments = DepartmentFilter(request.GET,queryset=department_data_all).qs
        # Extract data to list for response
        department_context_list=[]
        for department in departments:
            department_context_list.append(department.context_data)
        return Response({
            "status": True,
            "message": "Success",
            "data": department_context_list
            }
            
            , status=status.HTTP_200_OK)


class InstructorApiView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        if not check_permission(request):
            return Response({
                "status": False,
                "error": "Authentication failed due to the following reason: invalid token. Confirm that the access token in the authorization header is valid."
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        if not update_api_limit(request.headers['Application-Key'],datetime.now().hour):
            return Response({
            "status": False,
            "error": "Api request limit"
            }, status=status.HTTP_408_REQUEST_TIMEOUT)

        instructor_data_all = Instructor.objects.all()
        # Get all data by use filter
        instructors = InstructorFilter(request.GET,queryset=instructor_data_all).qs
        # Extract data to list for response
        instructor_context_list=[]
        for instructor in instructors:
            instructor_context_list.append(instructor.context_data)
        
        for instructor_data in instructor_context_list:
            instructor_data['department'] = instructor_data['department'].dname_th

        return Response({
            "status": True,
            "message": "Success",
            "data": instructor_context_list
            }
            
            , status=status.HTTP_200_OK)


class ReportStdGenderApiView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        if not check_permission(request):
            return Response({
                "status": False,
                "error": "Authentication failed due to the following reason: invalid token. Confirm that the access token in the authorization header is valid."
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        if not update_api_limit(request.headers['Application-Key'],datetime.now().hour):
            return Response({
            "status": False,
            "error": "Api request limit"
            }, status=status.HTTP_408_REQUEST_TIMEOUT)

        student_male_all = StudentShowdetail3.objects.filter(title_name_len='Mr.')
        student_female_all = StudentShowdetail3.objects.filter(title_name_len='Miss.')
        student_all = StudentShowdetail3.objects.all()
        
        return Response({
            "status": True,
            "message": "Success",
            "data" : [
            {
                "Gender": "Male",
                "Total": len(student_male_all)
            },
            {
                "Gender": "Female",
                "Total": len(student_female_all)
            },
            {
                "Gender": "All",
                "Total": len(student_all)
            },
            ]
            }, status=status.HTTP_200_OK)


class ReportStdAdyearApiView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        if not check_permission(request):
            return Response({
                "status": False,
                "error": "Authentication failed due to the following reason: invalid token. Confirm that the access token in the authorization header is valid."
            }, status=status.HTTP_401_UNAUTHORIZED)

        if not update_api_limit(request.headers['Application-Key'],datetime.now().hour):
            return Response({
            "status": False,
            "error": "Api request limit"
            }, status=status.HTTP_408_REQUEST_TIMEOUT)

        std_code_list = StudentShowdetail3.objects.values_list('std_code', flat=True).distinct()
        adyear_list = []
        adyear_dict = {}
        for std_code in std_code_list:
            if not std_code[:2] in adyear_list:
                adyear_list.append(std_code[:2])
                adyear_dict['25'+std_code[:2]] = 0
        std_all = StudentShowdetail3.objects.all()
        for std in std_all:
            adyear_dict['25'+std.std_code[:2]] += 1

        return Response({
            "status": True,
            "message": "Success",
            "data" : adyear_dict
            }
            , status=status.HTTP_200_OK)