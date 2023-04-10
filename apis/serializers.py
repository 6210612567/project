# from .models import Task
from .models import StuStudent,PrgPerPerson,PrgPerPersonDetail
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StuStudent
        fields = ('fname_th', 'lname_th', 'fname_en','lname_en' , 'nickname', 'email')


    def update(self, instance, validated_data):
        # * PeriodicTask Info
        instance.fname_th = validated_data.get(
            'fname_th', instance.fname_th)
        instance.lname_th = validated_data.get(
            'lname_th', instance.lname_th)
        instance.fname_en = validated_data.get(
            'fname_en', instance.fname_en)
        instance.lname_en = validated_data.get(
            'lname_en', instance.lname_en)
        instance.nickname = validated_data.get(
            'nickname', instance.nickname)
        instance.email = validated_data.get(
            'email', instance.email)
        instance.save()

        return instance
    

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrgPerPerson
        fields = ('fname_t', 'lname_t', 'fname_e','lname_e' , 'title', 'department', 'title_academic', 'ad_user')


    def update(self, instance, validated_data):
        # * PeriodicTask Info
        instance.fname_t = validated_data.get(
            'fname_t', instance.fname_t)
        instance.lname_t = validated_data.get(
            'lname_t', instance.lname_t)
        instance.fname_e = validated_data.get(
            'fname_e', instance.fname_e)
        instance.lname_e = validated_data.get(
            'lname_e', instance.lname_e)
        instance.title = validated_data.get(
            'title', instance.title)
        instance.department = validated_data.get(
            'department', instance.department)
        instance.title_academic = validated_data.get(
            'title_academic', instance.title_academic)
        instance.ad_user = validated_data.get(
            'ad_user', instance.ad_user)
        instance.save()

        return instance
    

class InstructorEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrgPerPersonDetail
        fields = ('email', )


    def update(self, instance, validated_data):
        # * PeriodicTask Info
        instance.email = validated_data.get(
            'email', instance.email)
        instance.save()

        return instance