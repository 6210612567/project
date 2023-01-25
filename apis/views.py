import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apis.custom.apis import Is2FAAuthenticated


from .authentication import ldap3_authen
# from rest_framework import permissions

# from django.contrib.auth.models import User

# MariadDB connect
import mariadb
import sys

# Import models
from web.models import major as Major , StudentShowdetail3 , department as Department ,instructor as Instructor
from .filter import MajorFilter,StudentShowdetail3Filter,DepartmentFilter,InstructorFilter




class AuthenticationApiView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        response = ldap3_authen(request.data['username'],request.data['password'])
        if response[0] == True:
            return Response({'name':response[1]}, status=status.HTTP_200_OK)
        else:
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        

############### NEW FIND STUDENT DATA BY USING DJANGO FILTER ###############
class StudentDataApiView(APIView):
    permission_classes = [Is2FAAuthenticated]

    def get(self, request, *args, **kwargs):
        student_data_all = StudentShowdetail3.objects.all()
        # Get all data by use filter
        students = StudentShowdetail3Filter(request.GET,queryset=student_data_all).qs
        # Extract data to list for response
        student_context_list=[]
        for student in students:
            student_context_list.append(student.context_data)
        return Response({'output':student_context_list}, status=status.HTTP_200_OK)


class MajorApiView(APIView):
    permission_classes = [Is2FAAuthenticated]

    def get(self, request, *args, **kwargs):
        major_data_all = Major.objects.all()
        # Get all data by use filter
        majors = MajorFilter(request.GET,queryset=major_data_all).qs
        # Extract data to list for response
        major_context_list=[]
        for major in majors:
            major_context_list.append(major.context_data)
        return Response({'output':major_context_list}, status=status.HTTP_200_OK)


class DepartmentApiView(APIView):
    permission_classes = [Is2FAAuthenticated]

    def get(self, request, *args, **kwargs):
        department_data_all = Department.objects.all()
        # Get all data by use filter
        departments = DepartmentFilter(request.GET,queryset=department_data_all).qs
        # Extract data to list for response
        department_context_list=[]
        for department in departments:
            department_context_list.append(department.context_data)
        return Response({'output':department_context_list}, status=status.HTTP_200_OK)


class InstructorApiView(APIView):
    permission_classes = [Is2FAAuthenticated]

    def get(self, request, *args, **kwargs):
        instructor_data_all = Instructor.objects.all()
        # Get all data by use filter
        instructors = InstructorFilter(request.GET,queryset=instructor_data_all).qs
        # Extract data to list for response
        instructor_context_list=[]
        for instructor in instructors:
            instructor_context_list.append(instructor.context_data)
        
        for instructor_data in instructor_context_list:
            instructor_data['department'] = instructor_data['department'].dname_th
        print('1')
        return Response({'output':instructor_context_list}, status=status.HTTP_200_OK)


class ReportStdGenderApiView(APIView):
    permission_classes = [Is2FAAuthenticated]

    def get(self, request, *args, **kwargs):
        student_male_all = StudentShowdetail3.objects.filter(title_name_len='Mr.')
        student_female_all = StudentShowdetail3.objects.filter(title_name_len='Miss.')
        student_all = StudentShowdetail3.objects.all()
        
        return Response(
            [
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
            , status=status.HTTP_200_OK)


class ReportStdAdyearApiView(APIView):
    permission_classes = [Is2FAAuthenticated]

    def get(self, request, *args, **kwargs):
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

        return Response(adyear_dict, status=status.HTTP_200_OK)