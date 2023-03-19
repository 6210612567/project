from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



############## Model For Web ##############

class AuthInfo(models.Model):
    secret_key = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    status = status = models.BooleanField(default=False)

    def __str__(self):
        return f"AuthInfo : {self.user} status : {self.status}"


class ChannelForAPI(models.Model):
    name = models.CharField(max_length=100 ,blank=False, null=False)
    desc = models.TextField(blank=True, null=True)
    auth_key = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=False)
    user = models.CharField(max_length=255)
    limit = models.IntegerField(max_length=255,default=3000)
    limit_time = models.IntegerField(max_length=2,default=0)

    @property
    def context_data(self):
        return {
            'name': self.name,
            'desc': self.desc,
            'status': self.status,
            'user': self.user,

        }

    def __str__(self):
        return f"Channels : {self.name}({self.user}) status : {self.status}"