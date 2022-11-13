from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class major(models.Model):
    mname_th = models.CharField(max_length=50)
    mname_en = models.CharField(max_length=50)
    def __str__(self):
        return f"[{self.id}] : {self.mname_th} ({self.mname_en})"

class department(models.Model):
    dname_th = models.CharField(max_length=50)
    dname_en = models.CharField(max_length=50)
    def __str__(self):
        return f"[{self.id}] : {self.dname_th} ({self.dname_en})"   


class instructor(models.Model):
    fname_th = models.CharField(max_length=50)
    lname_th = models.CharField(max_length=50)
    fname_en = models.CharField(max_length=50)
    lname_en = models.CharField(max_length=50)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
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