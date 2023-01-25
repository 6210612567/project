import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import *
from django.urls import reverse
from rest_framework import status
from .utils import check_2_factor_authen


# Goold Authenticator
import pyotp
import time
from django.http import JsonResponse
from .models import AuthInfo, ChannelForAPI
import qrcode
import json
from io import BytesIO
import base64
from django.http import HttpResponseRedirect


# Create your views here.
HOST = "http://127.0.0.1:8000"


def index(request):
    try:
        if request.session['user_id']:
            # print(request.session['user_id'])
            return HttpResponseRedirect(reverse("web:home"))
    except Exception as e:
        print(e)
        return render(request, "web/index.html")


def login_view(request):
    try:
        if request.session['user_id']:
            # print(request.session['user_id'])
            return render(request, "web/index2.html")
    except:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            # response = ldap3_authen(username,password)
            data = {
                'username': username,
                'password': password
            }
            response = requests.post(
                HOST+'/api/v1/authentication/', data=data)
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
        # print(request.session['user_id'])
        # print(e)
        return render(request, "web/index.html")


def setting_page(request):
    return render(request, "web/setting.html")


def privacy_page(request):
    return render(request, "web/privacy.html")


def home(request):
    channels = ChannelForAPI.objects.filter(user=request.session['user_id'])
    channels_open = ChannelForAPI.objects.filter(
        user=request.session['user_id'], status=True)
    channels_close = ChannelForAPI.objects.filter(
        user=request.session['user_id'], status=False)
    return render(request, "web/home.html", {
        'num_channel': len(channels),
        'num_open_channel': len(channels_open),
        'num_close_channel': len(channels_close),
    })


def channel_page(request):
    return render(request, "web/channel.html")


def documents(request):
    return render(request, "web/documents.html")


def document(request):
    return render(request, "web/document.html")


def report_page(request):
    channels = ChannelForAPI.objects.filter(user=request.session['user_id'])
    channels_open = ChannelForAPI.objects.filter(
        user=request.session['user_id'], status=True)
    channels_close = ChannelForAPI.objects.filter(
        user=request.session['user_id'], status=False)
    return render(request, "web/report.html", {
        'num_channel': len(channels),
        'num_open_channel': len(channels_open),
        'num_close_channel': len(channels_close),
    })


def help_page(request):
    return render(request, "web/help.html")


def update_page(request):
    return render(request, "web/update.html")


def getStart_page(request):
    return render(request, "web/documentsGettingStart.html")


def twoFactor_page(request):
    return render(request, "web/documentsTwoFactor.html")


def general(request):
    return render(request, "web/documentsGeneral.html")


def getting_auth(request):
    return render(request, "web/documentsGettingAuth.html")


def student(request):
    return render(request, "web/student.html")


def gettingStudentinfo(request):
    return render(request, "web/gettingStudentinfo.html")


def gettingStudentMajor(request):
    return render(request, "web/gettingStudentMajor.html")


def gettingStudentDepartment(request):
    return render(request, "web/gettingStudentDepartment.html")


def test_page(request, pin):
    try:
        authtor = AuthInfo.objects.get(user=request.session['user_id'])
        secret_key = authtor.secret_key
    except:
        secret_key = pyotp.random_base32()
        AuthInfo.objects.create(
            user=request.session['user_id'], secret_key=secret_key)
    # Check TOTP
    totp = pyotp.TOTP(secret_key)
    # Create QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(secret_key)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # Save img and convert to str for sent to frontend and render
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("ascii")

    return render(request, "web/test_page.html", {'data': {'status': 'True' if totp.verify(pin) else 'False', 'image': img_str}})


def createChannel_page(request):
    try:
        if request.session['user_id']:
            pass
    except Exception as e:
        # print(request.session['user_id'])
        # print(e)
        return render(request, "web/index.html")
    try:
        # data =json.loads(request.body)
        search_keyword = request.GET.get('search_keyword')
        # search_keyword = data["search_keyword"]
        channels = ChannelForAPI.objects.filter(
            user=request.session['user_id'], name__icontains=search_keyword)
    except:
        channels = ChannelForAPI.objects.filter(
            user=request.session['user_id'])
    channel_lists = []
    for channel in channels:
        channel_lists.append(channel)
    print(channel_lists)
    return render(request, "web/authkey.html", {'channel_list': channel_lists})


def insert_channel_view(request):
    data = json.loads(request.body)
    pin = data['pin']
    user_id = data['user_id']
    chname = data['chname']
    chdesc = data['chdesc']
    # Check 2FA Pin
    response = check_2_factor_authen(user_id, pin)
    if response['status'] == 'True':
        # Check if user's channel < 20 channel
        channels = ChannelForAPI.objects.filter(user=user_id)
        if len(channels) < 20:
            # Create Channel
            ChannelForAPI.objects.create(
                name=chname, desc=chdesc, user=user_id, status=False)
            data = {'status': 'True'}
        else:
            data = {'status': 'Full'}
        # Reture Status If channel created
        response = JsonResponse(data)
        response['X-Frame-Options'] = 'SAMEORIGIN'
        return response
    else:
        # Reture Status If channel not created
        data = {'status': 'False'}
        response = JsonResponse(data)
        response['X-Frame-Options'] = 'SAMEORIGIN'
        return response


def edit_channel_view(request):
    data = json.loads(request.body)
    pin = data['pin']
    user_id = data['user_id']
    chid = data['chid']
    chname = data['chname']
    chdesc = data['chdesc']
    chstatus = data['chstatus']
    # Check 2FA Pin
    response = check_2_factor_authen(user_id, pin)
    if response['status'] == 'True':
        # Create Channel
        channel = ChannelForAPI.objects.get(id=chid)
        # Reture Status If channel created
        channel.name = chname
        channel.desc = chdesc
        channel.status = chstatus
        if chstatus == 'True':
            auth_key = "TU//ENGR//"+pyotp.random_base32()
            channel.auth_key = auth_key
            data_res = {'status': 'แก้ไขข้อมูลแชนแนลแล้ว'}
        else:
            channel.auth_key = ""
            data_res = {'status': 'แก้ไขข้อมูลแชนแนลแล้ว'}
        channel.save()

        response = JsonResponse(data_res)
        response['X-Frame-Options'] = 'SAMEORIGIN'
        return response
    else:
        # Reture Status If channel not created
        data = {'status': 'False'}
        response = JsonResponse(data)
        response['X-Frame-Options'] = 'SAMEORIGIN'
        return response


def delete_channel_view(request, channel_id):
    try:
        channel = ChannelForAPI.objects.get(
            id=channel_id, user=request.session['user_id'])
        channel.delete()
        return HttpResponseRedirect(reverse("web:createChannel_page"))
    except:
        return HttpResponseRedirect(reverse("web:createChannel_page"))
 
def activate_2fac_view(request):
    auth = AuthInfo.objects.get(user=request.session['user_id'])
    auth.status = True
    auth.save()
    return HttpResponseRedirect(reverse("web:setting_page"))

def delete_2fac_view(request):
    auth = AuthInfo.objects.get(user=request.session['user_id'])
    auth.delete()
    return HttpResponseRedirect(reverse("web:setting_page"))
