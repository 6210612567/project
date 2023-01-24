from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class major(models.Model):
    mname_th = models.CharField(max_length=50)
    mname_en = models.CharField(max_length=50)

    @property
    def context_data(self):
        return {
            'id': self.id,
            'mname_th': self.mname_th,
            'mname_en': self.mname_en
        }

    def __str__(self):
        return f"[{self.id}] : {self.mname_th} ({self.mname_en})"

class department(models.Model):
    dname_th = models.CharField(max_length=50)
    dname_en = models.CharField(max_length=50)
    
    @property
    def context_data(self):
        return {
            'id': self.id,
            'dname_th': self.dname_th,
            'dname_en': self.dname_en
        }

    def __str__(self):
        return f"[{self.id}] : {self.dname_th} ({self.dname_en})"   


class instructor(models.Model):
    fname_th = models.CharField(max_length=50)
    lname_th = models.CharField(max_length=50)
    fname_en = models.CharField(max_length=50)
    lname_en = models.CharField(max_length=50)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)

    @property
    def context_data(self):
        return {
            'id': self.id,
            'fname_th': self.fname_th,
            'lname_th': self.lname_th,
            'fname_en': self.fname_en,
            'lname_en': self.lname_en,
            'department': self.department,
            'email': self.email,

        }


    def __str__(self):
        return f"[{self.id}] : {self.fname_th} {self.lname_th} ({self.fname_en} {self.lname_en}) at {self.department.dname_th} @ {self.email}"


class student(models.Model):
    # replyto = models.ForeignKey('thread.Thread', on_delete=models.CASCADE)
    status_is_graduated = models.BooleanField(default=False)
    student_code = models.IntegerField(blank=False, null=False)
    fname_th = models.CharField(max_length=50)
    lname_th = models.CharField(max_length=50)
    fname_en = models.CharField(max_length=50)
    lname_en = models.CharField(max_length=50)
    major = models.ForeignKey(major, on_delete=models.CASCADE)
    advisor = models.ForeignKey(instructor, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)

    # date = models.DateTimeField()
    # report = models.IntegerField(default=0)

    def __str__(self):
        return f"[{self.id}:{self.status_is_graduated}] : {self.fname_th} {self.lname_th} ({self.fname_en} {self.lname_en}) , at {self.department.dname_th} , @ {self.email} advisor => {self.advisor.fname_th} {self.advisor.lname_th} , major => {self.major.mname_th}"

    class Meta:
        ordering = ['student_code']

class StudentShowdetail3(models.Model):
    std_code = models.CharField(primary_key=True, max_length=15)
    tittle_name_lth = models.CharField(max_length=20, blank=True, null=True)
    title_name_len = models.CharField(max_length=20, blank=True, null=True)
    fname_th = models.CharField(max_length=255, blank=True, null=True)
    lname_th = models.CharField(max_length=255, blank=True, null=True)
    fname_en = models.CharField(max_length=255, blank=True, null=True)
    lname_en = models.CharField(max_length=255, blank=True, null=True)
    major_th = models.CharField(max_length=100, blank=True, null=True)
    major_en = models.CharField(max_length=100, blank=True, null=True)
    department_th = models.CharField(max_length=100, blank=True, null=True)
    department_en = models.CharField(max_length=100, blank=True, null=True)
    advisor_id = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    @property
    def context_data(self):
        return {
            'std_code': self.std_code,
            'tittle_name_lth': self.tittle_name_lth,
            'title_name_len': self.title_name_len,
            'fname_th': self.fname_th,
            'lname_th': self.lname_th,
            'fname_en': self.fname_en,
            'lname_en': self.lname_en,
            'major_th': self.major_th,
            'major_en': self.major_en,
            'department_th': self.department_th,
            'department_en': self.department_en,
            'advisor_id': self.advisor_id,
            'email': self.email,
        }

    class Meta:
        managed = False
        db_table = 'student_showdetail3'


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