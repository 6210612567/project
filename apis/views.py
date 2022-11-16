import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .authentication import ldap3_authen
# from rest_framework import permissions

# from django.contrib.auth.models import User

# MariadDB connect
import mariadb
import sys

# Import models
from web.models import major as Major , StudentShowdetail3
from .filter import MajorFilter,StudentShowdetail3Filter


class AuthenticationApiView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        response = ldap3_authen(request.data['username'],request.data['password'])
        if response[0] == True:
            return Response({'name':response[1]}, status=status.HTTP_200_OK)
        else:
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        

# OLD FIND STUDENT DATA
# class StudentDataApiView(APIView):
#     permission_classes = []

#     def get(self, request, *args, **kwargs):
#         # Connect to MariaDB Platform
#         std_code = request.query_params['std_code']
#         txt = ""
#         try:
#             conn = mariadb.connect(
#                 user="root",
#                 password="toor",
#                 host="127.0.0.1",
#                 port=3307,
#                 database="maraidb_project"
#             )
#             txt = "Connect Complete"
#         except mariadb.Error as e:
#             print(f"Error connecting to MariaDB Platform: {e}")
#             txt = f"Error connecting to MariaDB Platform: {e}"
#             sys.exit(1)

#         # Get Cursor
#         cur = conn.cursor()
#         cur.execute(f"SELECT * FROM student_showdetail3 WHERE std_code={std_code}")
#         fetch_data = cur.fetchone()
#         num_fields = len(fetch_data)
#         output = []
#         for index in range (0,num_fields):
#             output.append({cur.description[index][0]:fetch_data[index]})
#         return Response({'output':output}, status=status.HTTP_200_OK)


# NEW FIND STUDENT DATA BY USING DJANGO FILTER
class StudentDataApiView(APIView):
    permission_classes = []

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
    permission_classes = []

    def get(self, request, *args, **kwargs):
        major_data_all = Major.objects.all()
        # Get all data by use filter
        majors = MajorFilter(request.GET,queryset=major_data_all).qs
        # Extract data to list for response
        major_context_list=[]
        for major in majors:
            major_context_list.append(major.context_data)
        return Response({'output':major_context_list}, status=status.HTTP_200_OK)



