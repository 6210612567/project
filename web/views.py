from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import *
from django.urls import reverse
from .authentication import ldap3_authen
# Create your views here.

def index(request):
    return render(request, "web/index.html")


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("web:index"))

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        response = ldap3_authen(username,password)
        if response[0] == True:
            return render(request, "web/index.html",{'name':response[1]})
        else:
            return render(request, "web/login.html")
    return render(request, "web/login.html")
    

