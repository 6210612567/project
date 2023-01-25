from django import template
from web.models import AuthInfo
import pyotp
import time
import qrcode
import json
from io import BytesIO
import base64
# from grade.models import CustomGradeField,Grade


register = template.Library()

@register.filter
def get_2_factor_authen_qrcode(user_id):

    try:
        authtor = AuthInfo.objects.get(user=user_id)
        secret_key = authtor.secret_key
    except:
        secret_key = pyotp.random_base32()
        AuthInfo.objects.create(user=user_id,secret_key=secret_key)
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(f"otpauth://totp/{user_id}?secret={secret_key}")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("ascii")

    return img_str


@register.filter
def if_2_factor_authen(user_id):
    try:
        AuthInfo.objects.get(user=user_id,status=True)
        return True
    except:
        return False


@register.filter
def delete_2_factor_authen(user_id):
    try:
        authtor = AuthInfo.objects.get(user=user_id)
        authtor.delete()
        return True
    except:
        return False
