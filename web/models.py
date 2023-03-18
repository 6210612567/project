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


class engr_titlename(models.Model):
    titleid = models.IntegerField(primary_key=True)
    title_name_t = models.CharField(max_length=50)
    title_name_e = models.CharField(max_length=50)
    
    @property
    def context_data(self):
        return {
            'titleid': self.titleid,
            'title_name_t': self.title_name_t,
            'title_name_e': self.title_name_e
        }

    def __str__(self):
        return f"[{self.titleid}] : {self.title_name_t} ({self.title_name_e})"   


class engr_department(models.Model):
    departmentid = models.IntegerField(primary_key=True)
    departmentname = models.CharField(max_length=255)
    
    @property
    def context_data(self):
        return {
            'departmentid': self.departmentid,
            'departmentname': self.departmentname
        }

    def __str__(self):
        return f"[{self.departmentid}] : {self.departmentname} "   


class engr_leveleducation(models.Model):
    levelid = models.IntegerField(primary_key=True)
    levelname = models.CharField(max_length=255)
    
    @property
    def context_data(self):
        return {
            'levelid': self.departmentid,
            'levelname': self.levelname
        }

    def __str__(self):
        return f"[{self.levelid}] : {self.levelname} "   


class per_person(models.Model):
    personid = models.CharField(max_length=10, primary_key=True)
    title = models.IntegerField()
    fname_t = models.CharField(max_length=255)
    lname_t = models.CharField(max_length=255)
    fname_e = models.CharField(max_length=255)
    lname_e = models.CharField(max_length=255)
    department = models.IntegerField()
    title_academic = models.IntegerField()
    ad_user = models.CharField(max_length=15)


class instructor(models.Model):
    fname_th = models.CharField(max_length=50)
    lname_th = models.CharField(max_length=50)
    fname_en = models.CharField(max_length=50)
    lname_en = models.CharField(max_length=50)
    department = models.ForeignKey(engr_department, on_delete=models.CASCADE)
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
            'fname_th': self.fname_th,
            'lname_th': self.lname_th,
            'fname_en': self.fname_en,
            'lname_en': self.lname_en,
            'advisor_id': self.advisor_id,
            'email': self.email,
        }

    class Meta:
        
        managed = False
        db_table = 'student_showdetail3'


class engr_student(models.Model):
    std_code = models.CharField(primary_key=True, max_length=15)
    title_id = models.CharField(max_length=3)
    fname_th = models.CharField(max_length=255, blank=True, null=True)
    lname_th = models.CharField(max_length=255, blank=True, null=True)
    fname_en = models.CharField(max_length=255, blank=True, null=True)
    lname_en = models.CharField(max_length=255, blank=True, null=True)
    degree_id = models.CharField(max_length=1, blank=True, null=True)
    department_id = models.CharField(max_length=3, blank=True, null=True)
    advisor_id = models.CharField(max_length=10, blank=True, null=True)
    citizen_id = models.CharField(max_length=20)
    birthdate = models.CharField(max_length=10)
    religion_id = models.CharField(max_length=1)
    nation_id = models.CharField(max_length=1)
    sex = models.CharField(max_length=1)
    nickname = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    reg_address = models.CharField(max_length=255)
    reg_road = models.CharField(max_length=255)
    reg_subdistrict = models.CharField(max_length=255)
    reg_amphur = models.CharField(max_length=255)
    reg_province_id = models.CharField(max_length=2)
    reg_telephone = models.CharField(max_length=15)
    reg_postcode = models.CharField(max_length=5)
    cur_address = models.CharField(max_length=255)
    cur_road = models.CharField(max_length=255)
    cur_subdistrict = models.CharField(max_length=255)
    cur_amphur = models.CharField(max_length=255)
    cur_province_id = models.CharField(max_length=2)
    cur_postcode = models.CharField(max_length=5)
    fat_fname = models.CharField(max_length=255)
    fat_lname = models.CharField(max_length=255)
    fat_year = models.CharField(max_length=3)
    fat_address = models.CharField(max_length=255)
    fat_road = models.CharField(max_length=255)
    fat_subdistrict = models.CharField(max_length=255)
    fat_amphur = models.CharField(max_length=255)
    fat_province_id = models.CharField(max_length=2)
    fat_postcode = models.CharField(max_length=5)
    fat_telephone = models.CharField(max_length=30)
    fat_occupation = models.CharField(max_length=150)
    fat_position = models.CharField(max_length=150)
    fat_status = models.CharField(max_length=2)
    fat_type = models.CharField(max_length=255)
    fat_salary = models.CharField(max_length=10)
    fat_comname = models.CharField(max_length=255)
    fat_compro = models.CharField(max_length=3)
    fat_idcard = models.CharField(max_length=20)
    mot_fname = models.CharField(max_length=255)
    mot_lname = models.CharField(max_length=255)
    mot_year = models.CharField(max_length=3)
    mot_status = models.CharField(max_length=3)
    mot_address = models.CharField(max_length=255)
    mot_road = models.CharField(max_length=255)
    mot_subdistrict = models.CharField(max_length=255)
    mot_amphur = models.CharField(max_length=255)
    mot_province_id = models.CharField(max_length=2)
    mot_postcode = models.CharField(max_length=5)
    mot_telephone = models.CharField(max_length=30)
    mot_occupation = models.CharField(max_length=150)
    mot_position = models.CharField(max_length=150)
    mot_type = models.CharField(max_length=255)
    mot_salary = models.CharField(max_length=10)
    mot_comname = models.CharField(max_length=255)
    mot_compro = models.CharField(max_length=3)
    mot_idcard = models.CharField(max_length=20)
    gus_fname = models.CharField(max_length=255)
    gus_lname = models.CharField(max_length=255)
    gus_relation = models.CharField(max_length=10)
    gus_occupation = models.CharField(max_length=150)
    gus_position = models.CharField(max_length=255)
    gus_address = models.CharField(max_length=255)
    gus_road = models.CharField(max_length=255)
    gus_subdistrict = models.CharField(max_length=255)
    gus_amphur = models.CharField(max_length=255)
    gus_province_id = models.CharField(max_length=2)
    gus_postcode = models.CharField(max_length=5)
    gus_telephone = models.CharField(max_length=30)
    con_fname = models.CharField(max_length=255)
    con_lname = models.CharField(max_length=255)
    con_address = models.CharField(max_length=255)
    con_road = models.CharField(max_length=255)
    con_subdistrict = models.CharField(max_length=255)
    con_amphur = models.CharField(max_length=255)
    con_province_id = models.CharField(max_length=2)
    con_postcode = models.CharField(max_length=5)
    con_telephone = models.CharField(max_length=30)
    con_relation = models.CharField(max_length=30)
    con_occupation = models.CharField(max_length=255)
    con_position = models.CharField(max_length=255)
    uppic = models.CharField(max_length=3)
    sch_old = models.CharField(max_length=255)
    sch_pro = models.CharField(max_length=100)
    prinfo = models.CharField(max_length=10)
    tuemail = models.EmailField()
    bankid = models.CharField(max_length=3)
    bankno = models.CharField(max_length=20)


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