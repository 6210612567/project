import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import *
from django.urls import reverse
from rest_framework import status

# Create your views here.
HOST = "http://127.0.0.1:8000"



def index(request):
    return render(request, "web/index.html")


def login_view(request):
    try:
        if request.session['user_id']:
            return HttpResponseRedirect(reverse("web:index"))
    except:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            # response = ldap3_authen(username,password)
            data = {
                'username' : username,
                'password' : password
            }
            response = requests.post('http://127.0.0.1:8000/api/v1/authentication/', data=data)
            if response.status_code == status.HTTP_200_OK:
                request.session['user_id'] = username
                request.session['login_status'] = username
                return render(request, "web/index.html",{'name':response.json()['name']})
            else:
                return render(request, "web/login.html")
        return render(request, "web/login.html")

