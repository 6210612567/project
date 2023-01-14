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
