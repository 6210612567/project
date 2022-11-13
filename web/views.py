import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import *
from django.urls import reverse
from rest_framework import status

# Create your views here.
HOST = "http://127.0.0.1:8000"



def index(request):
    try:
        if request.session['user_id']:
            # print(request.session['user_id'])
            return render(request, "web/home.html",{'name':request.session['user_id']})
    except Exception as e:
        print(e)
        return render(request, "web/index.html")


def login_view(request):
    try:
        if request.session['user_id']:
            # print(request.session['user_id'])
            return render(request, "web/index2.html",{'name':response.json()['name']})
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
                print(request.session['user_id'])
                # print("render policy page")
                request.session['login_status'] = username
                request.session.modified = True
                # return render(request, "web/policy.html")
                return HttpResponseRedirect(reverse("web:pdpa_page"))
            else:
                return render(request, "web/login.html")
        return render(request, "web/login.html")

def logout_view(request):
    del request.session['user_id']
    return HttpResponseRedirect(reverse("web:index"))

def pdpa_page(request):
    try:
        if request.session['user_id']:
            return render(request, "web/policy.html")
    except Exception as e:
        print(request.session['user_id'])
        print(e)
        return render(request, "web/index.html")
