from django.contrib import admin

# Register your models here.
from django.apps import apps
from .models import *

# models = apps.get_models()

# for model in models:
#     admin.site.register(model)

admin.site.register(student)
admin.site.register(department)
admin.site.register(instructor)
admin.site.register(major)