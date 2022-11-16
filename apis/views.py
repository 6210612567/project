import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .authentication import ldap3_authen
# from rest_framework import permissions
# from .models import Task
# from django.contrib.auth.models import User

# MariadDB connect
import mariadb
import sys



class AuthenticationApiView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        response = ldap3_authen(request.data['username'],request.data['password'])
        if response[0] == True:
            return Response({'name':response[1]}, status=status.HTTP_200_OK)
        else:
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        

class StudentDataApiView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        # Connect to MariaDB Platform
        std_code = request.query_params['std_code']
        txt = ""
        try:
            conn = mariadb.connect(
                user="root",
                password="toor",
                host="127.0.0.1",
                port=3307,
                database="maraidb_project"
            )
            txt = "Connect Complete"
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            txt = f"Error connecting to MariaDB Platform: {e}"
            sys.exit(1)

        # Get Cursor
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM student_showdetail3 WHERE std_code={std_code}")
        fetch_data = cur.fetchone()
        num_fields = len(fetch_data)
        output = []
        for index in range (0,num_fields):
            output.append({cur.description[index][0]:fetch_data[index]})
        return Response({'output':output}, status=status.HTTP_200_OK)



