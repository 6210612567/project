from django.contrib import admin

# Register your models here.
from django.apps import apps
from .models import *

# models = apps.get_models()

# for model in models:
#     admin.site.register(model)



admin.site.register(AuthInfo)
admin.site.register(ChannelForAPI)
