import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .authentication import ldap3_authen
# from rest_framework import permissions
# from .models import Task
# from django.contrib.auth.models import User



class AuthenticationApiView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        response = ldap3_authen(request.data['username'],request.data['password'])
        if response[0] == True:
            return Response({'name':response[1]}, status=status.HTTP_200_OK)
        else:
            return Response('Unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        
