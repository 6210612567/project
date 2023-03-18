# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EngrDepartment(models.Model):
    departmentid = models.IntegerField(primary_key=True)
    departmentname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'engr_department'


class EngrLeveleducation(models.Model):
    levelid = models.IntegerField(primary_key=True)
    levelname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'engr_leveleducation'


class EngrProvince(models.Model):
    idprovince = models.IntegerField(primary_key=True)
    province = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engr_province'


class EngrTitleacademic(models.Model):
    titleacaid = models.IntegerField(primary_key=True)
    titleacafullt = models.CharField(max_length=50)
    titleacafulle = models.CharField(max_length=50)
    titleacalitt = models.CharField(max_length=20)
    titleacalite = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'engr_titleacademic'


class EngrTitlename(models.Model):
    titleid = models.IntegerField(primary_key=True)
    title_name_t = models.CharField(max_length=50, db_collation='utf8mb4_unicode_ci')
    title_name_e = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'engr_titlename'


class ExtPerson(models.Model):
    personid = models.CharField(primary_key=True, max_length=10)
    title = models.IntegerField(blank=True, null=True)
    fname_t = models.CharField(max_length=255, blank=True, null=True)
    lname_t = models.CharField(max_length=255, blank=True, null=True)
    fname_e = models.CharField(max_length=255, blank=True, null=True)
    lname_e = models.CharField(max_length=255, blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=15, blank=True, null=True)
    idcard = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    dateadd = models.DateTimeField(blank=True, null=True)
    bankaccountid = models.CharField(max_length=20, blank=True, null=True)
    bankname = models.CharField(max_length=255, blank=True, null=True)
    taxid = models.CharField(max_length=30, blank=True, null=True)
    peopleid = models.CharField(max_length=50, blank=True, null=True)
    socialid = models.CharField(max_length=20, blank=True, null=True)
    grp = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ext_person'


class FinPersontax(models.Model):
    no = models.IntegerField(db_column='No')  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    dept = models.IntegerField(db_column='Dept', blank=True, null=True)  # Field name made lowercase.
    staffid = models.CharField(db_column='StaffID', max_length=11)  # Field name made lowercase.
    summoney = models.FloatField(db_column='SumMoney', blank=True, null=True)  # Field name made lowercase.
    sumtax = models.FloatField(db_column='SumTAX')  # Field name made lowercase.
    sumsocial = models.FloatField(db_column='SumSocial')  # Field name made lowercase.
    socialid = models.CharField(db_column='SocialID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    y = models.CharField(db_column='Y', max_length=11)  # Field name made lowercase.
    peapleid = models.CharField(db_column='PeapleID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fin-persontax'


class FinPersontaxref(models.Model):
    y = models.IntegerField(db_column='Y')  # Field name made lowercase.
    dateput = models.CharField(db_column='DatePut', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fin-persontaxref'


class FinTransfermoney(models.Model):
    autokey = models.FloatField()
    staffid = models.CharField(max_length=10, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    item = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    money = models.FloatField(blank=True, null=True)
    moneypay = models.FloatField(blank=True, null=True)
    tax = models.CharField(max_length=10, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    datepay = models.DateField(blank=True, null=True)
    datetax = models.DateField(blank=True, null=True)
    datesocial = models.DateField(blank=True, null=True)
    socialpay = models.FloatField(blank=True, null=True)
    staffidtransfer = models.CharField(max_length=10, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    tubankitem = models.FloatField(blank=True, null=True)
    office_acc = models.CharField(max_length=255, blank=True, null=True)
    tubankpay = models.FloatField(blank=True, null=True)
    fund = models.FloatField(db_column='Fund', blank=True, null=True)  # Field name made lowercase.
    waterelec = models.FloatField(db_column='WaterElec', blank=True, null=True)  # Field name made lowercase.
    chawporkor = models.FloatField(blank=True, null=True)
    assetoffice = models.FloatField(blank=True, null=True)
    water = models.FloatField(blank=True, null=True)
    fundadd = models.FloatField(blank=True, null=True)
    socialadd = models.FloatField(blank=True, null=True)
    notice = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    houserent = models.CharField(max_length=20, blank=True, null=True)
    slf = models.FloatField(db_column='SLF', blank=True, null=True)  # Field name made lowercase.
    icl = models.FloatField(db_column='ICL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fin-transfermoney'


class PerPerson(models.Model):
    personid = models.CharField(primary_key=True, max_length=10)
    title = models.IntegerField(blank=True, null=True)
    fname_t = models.CharField(max_length=255, blank=True, null=True)
    lname_t = models.CharField(max_length=255, blank=True, null=True)
    fname_e = models.CharField(max_length=255, blank=True, null=True)
    lname_e = models.CharField(max_length=255, blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    title_academic = models.IntegerField(blank=True, null=True)
    ad_user = models.CharField(max_length=15, blank=True, null=True)
    full_ad = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'per_person'


class PerPersonAddress(models.Model):
    personid = models.CharField(primary_key=True, max_length=10)
    curid = models.CharField(max_length=255, blank=True, null=True)
    curroad = models.CharField(max_length=255, blank=True, null=True)
    cursub = models.CharField(max_length=255, blank=True, null=True)
    curdis = models.CharField(max_length=255, blank=True, null=True)
    curpro = models.CharField(max_length=3, blank=True, null=True)
    curcountry = models.CharField(max_length=255, blank=True, null=True)
    curpost = models.CharField(max_length=6, blank=True, null=True)
    curtel = models.CharField(max_length=20, blank=True, null=True)
    curmobile = models.CharField(max_length=20, blank=True, null=True)
    homeid = models.CharField(max_length=255, blank=True, null=True)
    homeroad = models.CharField(max_length=255, blank=True, null=True)
    homesub = models.CharField(max_length=255, blank=True, null=True)
    homedis = models.CharField(max_length=255, blank=True, null=True)
    homepro = models.CharField(max_length=3, blank=True, null=True)
    homecountry = models.CharField(max_length=255, blank=True, null=True)
    homepost = models.CharField(max_length=6, blank=True, null=True)
    hometel = models.CharField(max_length=20, blank=True, null=True)
    homemobile = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'per_person_address'


class PerPersonDetail(models.Model):
    personid = models.CharField(primary_key=True, max_length=10)
    idcard = models.CharField(max_length=13, blank=True, null=True)
    birthdate = models.CharField(max_length=10, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    taxid = models.CharField(max_length=15, blank=True, null=True)
    socialid = models.CharField(max_length=15, blank=True, null=True)
    citizenship = models.CharField(max_length=15, blank=True, null=True)
    nationality = models.CharField(max_length=15, blank=True, null=True)
    religion = models.CharField(max_length=15, blank=True, null=True)
    extelphone = models.CharField(max_length=15, blank=True, null=True)
    rooms = models.CharField(max_length=10, blank=True, null=True)
    stayat = models.CharField(max_length=15, blank=True, null=True)
    cardstatus = models.CharField(max_length=1, blank=True, null=True)
    workstatus = models.CharField(max_length=2, blank=True, null=True)
    typeperson = models.CharField(max_length=5, blank=True, null=True)
    positionid = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    bankid = models.CharField(max_length=20, blank=True, null=True)
    bankname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    groupsalary = models.CharField(max_length=5, blank=True, null=True)
    docrefer = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    codeajarn = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'per_person_detail'


class PerPersonEducation(models.Model):
    id = models.IntegerField(primary_key=True)
    personid = models.CharField(max_length=10, blank=True, null=True)
    edulevel = models.CharField(max_length=2, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    eduname = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    educer = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    edumajor = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    edustart = models.CharField(max_length=10, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    eduend = models.CharField(max_length=10, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    edugpa = models.CharField(max_length=5, db_collation='utf8mb3_unicode_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'per_person_education'


class PerPersonExperience(models.Model):
    iddoc = models.IntegerField(primary_key=True)
    personid = models.CharField(max_length=10, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    name = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    address = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    position = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    start = models.CharField(max_length=10, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    end = models.CharField(max_length=10, db_collation='utf8mb3_unicode_ci', blank=True, null=True)
    jobdis = models.TextField(db_collation='utf8mb3_unicode_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'per_person_experience'


class PerPersonFamily(models.Model):
    id = models.IntegerField(primary_key=True)
    personid = models.CharField(max_length=10, blank=True, null=True)
    relation = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    idcard = models.CharField(max_length=15, blank=True, null=True)
    birthday = models.CharField(max_length=10, blank=True, null=True)
    cerid = models.CharField(max_length=15, blank=True, null=True)
    remark = models.CharField(max_length=10, blank=True, null=True)
    medical = models.CharField(max_length=3, blank=True, null=True)
    school = models.CharField(max_length=3, blank=True, null=True)
    job1 = models.CharField(max_length=255, blank=True, null=True)
    job2 = models.CharField(max_length=255, blank=True, null=True)
    where1 = models.CharField(max_length=255, blank=True, null=True)
    where2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'per_person_family'


class PerPersonIngov(models.Model):
    personid = models.CharField(primary_key=True, max_length=10)
    govid = models.CharField(max_length=10, blank=True, null=True)
    levelc = models.CharField(max_length=20, blank=True, null=True)
    leveledu = models.CharField(max_length=20, blank=True, null=True)
    applywork = models.CharField(max_length=100, blank=True, null=True)
    startwork = models.CharField(max_length=100, blank=True, null=True)
    applyfac = models.CharField(max_length=100, blank=True, null=True)
    startfac = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'per_person_ingov'


class PerPersonTraining(models.Model):
    iddoc = models.IntegerField(primary_key=True)
    personid = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    typecourse = models.CharField(max_length=2, db_collation='utf8mb3_general_ci', blank=True, null=True)
    titlename = models.TextField(db_collation='utf8mb3_general_ci', blank=True, null=True)
    place = models.TextField(db_collation='utf8mb3_general_ci', blank=True, null=True)
    start = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    end = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    deptowner = models.TextField(db_collation='utf8mb3_general_ci', blank=True, null=True)
    expense = models.TextField(db_collation='utf8mb3_general_ci', blank=True, null=True)
    source = models.TextField(db_collation='utf8mb3_general_ci', blank=True, null=True)
    dateadd = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)
    timeadd = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'per_person_training'


class PerPosition(models.Model):
    prositionid = models.IntegerField(primary_key=True)
    prositionname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'per_position'


class PerStatuswork(models.Model):
    statusworkid = models.IntegerField(primary_key=True)
    statusworkname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'per_statuswork'


class PerTypeperson(models.Model):
    typepersonid = models.IntegerField(primary_key=True)
    typepersonname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'per_typeperson'


class PerTypetraining(models.Model):
    idtype = models.CharField(primary_key=True, max_length=10)
    typename = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'per_typetraining'


class WebAuthinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    secret_key = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'web_authinfo'


class WebChannelforapi(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    auth_key = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    user = models.CharField(max_length=255)
    limit = models.IntegerField()
    limit_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'web_channelforapi'


class WebEngrDepartment(models.Model):
    departmentid = models.IntegerField(primary_key=True)
    departmentname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'web_engr_department'


class WebEngrLeveleducation(models.Model):
    levelid = models.IntegerField(primary_key=True)
    levelname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'web_engr_leveleducation'


class WebEngrTitlename(models.Model):
    titleid = models.IntegerField(primary_key=True)
    title_name_t = models.CharField(max_length=50)
    title_name_e = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'web_engr_titlename'


class WebInstructor(models.Model):
    id = models.BigAutoField(primary_key=True)
    fname_th = models.CharField(max_length=50)
    lname_th = models.CharField(max_length=50)
    fname_en = models.CharField(max_length=50)
    lname_en = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    department = models.ForeignKey(WebEngrDepartment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'web_instructor'


class WebMajor(models.Model):
    id = models.BigAutoField(primary_key=True)
    mname_th = models.CharField(max_length=50)
    mname_en = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'web_major'


class WebPerPerson(models.Model):
    personid = models.CharField(primary_key=True, max_length=10)
    title = models.IntegerField()
    fname_t = models.CharField(max_length=255)
    lname_t = models.CharField(max_length=255)
    fname_e = models.CharField(max_length=255)
    lname_e = models.CharField(max_length=255)
    department = models.IntegerField()
    title_academic = models.IntegerField()
    ad_user = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'web_per_person'
