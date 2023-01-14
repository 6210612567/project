from rest_framework.permissions import BasePermission
from web.models import ChannelForAPI

class Is2FAAuthenticated(BasePermission):

    def has_permission(self, request, view):
        try:
            auth_key = request.headers['Application-Key']
            ChannelForAPI.objects.get(auth_key=auth_key,status=True)
            return True
        except:
            return False

        