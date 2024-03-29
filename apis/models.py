from django.db import models

# Create your models here.


class PrgEngrDepartment(models.Model):
    departmentid = models.IntegerField(primary_key=True)
    departmentname = models.CharField(max_length=255)

    
    @property
    def context_data(self):
        return {
            'departmentid':self.departmentid,
            'departmentname': self.departmentname
        }

    class Meta:
        managed = False
        db_table = 'engr_department'


class PrgEngrLeveleducation(models.Model):
    levelid = models.IntegerField(primary_key=True)
    levelname = models.CharField(max_length=255)

    

    class Meta:
        managed = False
        db_table = 'engr_leveleducation'


class PrgEngrProvince(models.Model):
    idprovince = models.IntegerField(primary_key=True)
    province = models.CharField(max_length=100, blank=True, null=True)

    

    class Meta:
        managed = False
        db_table = 'engr_province'


class PrgEngrTitleacademic(models.Model):
    titleacaid = models.IntegerField(primary_key=True)
    titleacafullt = models.CharField(max_length=50)
    titleacafulle = models.CharField(max_length=50)
    titleacalitt = models.CharField(max_length=20)
    titleacalite = models.CharField(max_length=20)

    

    class Meta:
        managed = False
        db_table = 'engr_titleacademic'


class PrgEngrTitlename(models.Model):
    titleid = models.IntegerField(primary_key=True)
    title_name_t = models.CharField(max_length=50, db_collation='utf8mb4_unicode_ci')
    title_name_e = models.CharField(max_length=50)

    

    class Meta:
        managed = False
        db_table = 'engr_titlename'


class PrgExtPerson(models.Model):
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


class PrgFinPersontax(models.Model):
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


class PrgFinPersontaxref(models.Model):
    y = models.IntegerField(db_column='Y')  # Field name made lowercase.
    dateput = models.CharField(db_column='DatePut', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    

    class Meta:
        managed = False
        db_table = 'fin-persontaxref'


class PrgFinTransfermoney(models.Model):
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


class PrgPerPerson(models.Model):
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

    @property
    def context_data(self):
        return {
            'personid':self.personid,
            'title': self.title,
            'fname_t':self.fname_t,
            'lname_t': self.lname_t,
            'fname_e':self.fname_e,
            'lname_e': self.lname_e,
            'department':self.department,
            'title_academic': self.title_academic,
            'ad_user':self.ad_user,
            'full_ad': self.full_ad
        }


    class Meta:
        managed = False
        db_table = 'per_person'


class PrgPerPersonAddress(models.Model):
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


class PrgPerPersonDetail(models.Model):
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


class PrgPerPersonEducation(models.Model):
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


class PrgPerPersonExperience(models.Model):
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


class PrgPerPersonFamily(models.Model):
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


class PrgPerPersonIngov(models.Model):
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


class PrgPerPersonTraining(models.Model):
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


class PrgPerPosition(models.Model):
    prositionid = models.IntegerField(primary_key=True)
    prositionname = models.CharField(max_length=255)

    

    class Meta:
        managed = False
        db_table = 'per_position'


class PrgPerStatuswork(models.Model):
    statusworkid = models.IntegerField(primary_key=True)
    statusworkname = models.CharField(max_length=255)

    

    class Meta:
        managed = False
        db_table = 'per_statuswork'


class PrgPerTypeperson(models.Model):
    typepersonid = models.IntegerField(primary_key=True)
    typepersonname = models.CharField(max_length=255)

    

    class Meta:
        managed = False
        db_table = 'per_typeperson'


class PrgPerTypetraining(models.Model):
    idtype = models.CharField(primary_key=True, max_length=10)
    typename = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)

    

    class Meta:
        managed = False
        db_table = 'per_typetraining'


class PrgAddnewstudent(models.Model):
    stu_code = models.CharField(primary_key=True, max_length=10)
    title_id = models.CharField(max_length=50, blank=True, null=True)
    fname_th = models.CharField(max_length=255, blank=True, null=True)
    lname_th = models.CharField(max_length=255, blank=True, null=True)
    fname_en = models.CharField(max_length=255, blank=True, null=True)
    lname_en = models.CharField(max_length=255, blank=True, null=True)
    degree_id = models.CharField(max_length=10, blank=True, null=True)
    department_id = models.CharField(max_length=10, blank=True, null=True)
    advisor_id = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    schoolname = models.CharField(max_length=200, blank=True, null=True)
    schoolpro = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addnewstudent'


class PrgApplyebm(models.Model):
    idapp = models.CharField(primary_key=True, max_length=10)
    picname = models.CharField(max_length=255, blank=True, null=True)
    titlenamet = models.CharField(max_length=255)
    fnameth = models.CharField(max_length=255)
    lnameth = models.CharField(max_length=255)
    titlenamee = models.CharField(max_length=255)
    fnameeng = models.CharField(max_length=255)
    lnameeng = models.CharField(max_length=255)
    dateofbirth = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    relgion = models.CharField(max_length=255)
    nationality = models.CharField(max_length=1)
    idcard = models.CharField(max_length=13)
    othernationality = models.CharField(max_length=255, blank=True, null=True)
    idpassport = models.CharField(max_length=255, blank=True, null=True)
    nopresent = models.CharField(max_length=255)
    moopresent = models.CharField(max_length=5)
    bulpresent = models.CharField(max_length=255, blank=True, null=True)
    soipresent = models.CharField(max_length=255, blank=True, null=True)
    roodpresent = models.CharField(max_length=255, blank=True, null=True)
    subpresent = models.CharField(max_length=255, blank=True, null=True)
    dispresent = models.CharField(max_length=255, blank=True, null=True)
    propresent = models.CharField(max_length=255, blank=True, null=True)
    postpresent = models.CharField(max_length=5, blank=True, null=True)
    telpresent = models.CharField(max_length=255)
    mobilepresent = models.CharField(max_length=255)
    otheron = models.CharField(max_length=10, blank=True, null=True)
    othermoo = models.CharField(max_length=5, blank=True, null=True)
    otherbuilding = models.CharField(max_length=255, blank=True, null=True)
    othersoi = models.CharField(max_length=255, blank=True, null=True)
    otherroad = models.CharField(max_length=255, blank=True, null=True)
    othersub = models.CharField(max_length=255, blank=True, null=True)
    otherdir = models.CharField(max_length=255, blank=True, null=True)
    otherpro = models.CharField(max_length=255, blank=True, null=True)
    otherpost = models.CharField(max_length=255, blank=True, null=True)
    othertel = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    dadfname = models.CharField(max_length=255, blank=True, null=True)
    dadlname = models.CharField(max_length=255, blank=True, null=True)
    dadoccupation = models.CharField(max_length=255, blank=True, null=True)
    dadnameoffice = models.CharField(max_length=255, blank=True, null=True)
    dadposition = models.CharField(max_length=255, blank=True, null=True)
    dadtel = models.CharField(max_length=255, blank=True, null=True)
    dadaddress = models.CharField(max_length=255, blank=True, null=True)
    dademail = models.CharField(max_length=255, blank=True, null=True)
    momfname = models.CharField(max_length=255, blank=True, null=True)
    momlname = models.CharField(max_length=255, blank=True, null=True)
    momoccupation = models.CharField(max_length=255, blank=True, null=True)
    momnameoffice = models.CharField(max_length=255, blank=True, null=True)
    momposition = models.CharField(max_length=255, blank=True, null=True)
    momtel = models.CharField(max_length=255, blank=True, null=True)
    momaddress = models.CharField(max_length=255, blank=True, null=True)
    momemail = models.CharField(max_length=255, blank=True, null=True)
    parentfname = models.CharField(max_length=255, blank=True, null=True)
    parentlname = models.CharField(max_length=255, blank=True, null=True)
    parentoccupation = models.CharField(max_length=255, blank=True, null=True)
    parentnameoffice = models.CharField(max_length=255, blank=True, null=True)
    parentposition = models.CharField(max_length=255, blank=True, null=True)
    parenttel = models.CharField(max_length=255, blank=True, null=True)
    parentaddress = models.CharField(max_length=255, blank=True, null=True)
    parentemail = models.CharField(max_length=255, blank=True, null=True)
    secondaryname = models.CharField(max_length=255, blank=True, null=True)
    secondaryprovince = models.CharField(max_length=255, blank=True, null=True)
    secondaryacademic = models.CharField(max_length=255, blank=True, null=True)
    secondarygrade = models.CharField(max_length=5, blank=True, null=True)
    secondarystart = models.CharField(max_length=255, blank=True, null=True)
    secondaryend = models.CharField(max_length=255, blank=True, null=True)
    hightschoolname = models.CharField(max_length=255, blank=True, null=True)
    hightschoolprovince = models.CharField(max_length=255, blank=True, null=True)
    hightschoolacademic = models.CharField(max_length=255, blank=True, null=True)
    hightschoolgrade = models.CharField(max_length=5, blank=True, null=True)
    hightschoolstart = models.CharField(max_length=255, blank=True, null=True)
    hightschoolend = models.CharField(max_length=255, blank=True, null=True)
    award = models.TextField(blank=True, null=True)
    q1301 = models.CharField(max_length=5, blank=True, null=True)
    q1302 = models.CharField(max_length=5, blank=True, null=True)
    q1303 = models.CharField(max_length=5, blank=True, null=True)
    q1304 = models.CharField(max_length=5, blank=True, null=True)
    q1304text = models.CharField(max_length=255, blank=True, null=True)
    q1305 = models.CharField(max_length=5, blank=True, null=True)
    q1305text = models.CharField(max_length=255, blank=True, null=True)
    q1306 = models.CharField(max_length=5, blank=True, null=True)
    q1306text = models.CharField(max_length=255, blank=True, null=True)
    q1307 = models.CharField(max_length=5, blank=True, null=True)
    q1307text = models.CharField(max_length=255, blank=True, null=True)
    q1308 = models.CharField(max_length=5, blank=True, null=True)
    q1308text = models.CharField(max_length=255, blank=True, null=True)
    q1401fac = models.CharField(max_length=255, blank=True, null=True)
    q1401name = models.CharField(max_length=255, blank=True, null=True)
    q1402fac = models.CharField(max_length=255, blank=True, null=True)
    q1402name = models.CharField(max_length=255, blank=True, null=True)
    q1403fac = models.CharField(max_length=255, blank=True, null=True)
    q1403name = models.CharField(max_length=255, blank=True, null=True)
    q1404fac = models.CharField(max_length=255, blank=True, null=True)
    q1404name = models.CharField(max_length=255, blank=True, null=True)
    q15 = models.TextField(blank=True, null=True)
    q1601 = models.CharField(max_length=5, blank=True, null=True)
    q1601gade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    q1602 = models.CharField(max_length=5, blank=True, null=True)
    smartmath = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    smartread = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    smarteng = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    smartgen = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    oneteng = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    onetmath = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    onetsci = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gat = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pat1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pat3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sat1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sat2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dateadd = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    docinfac = models.DateTimeField(blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applyebm'


class PrgApplyebmmaster(models.Model):
    idapp = models.CharField(primary_key=True, max_length=10)
    planstudy = models.CharField(max_length=1, blank=True, null=True)
    inmajor = models.CharField(max_length=1, blank=True, null=True)
    titlethesis = models.CharField(max_length=255, blank=True, null=True)
    titlenamet = models.CharField(max_length=10, blank=True, null=True)
    fnameth = models.CharField(max_length=255, blank=True, null=True)
    lnameth = models.CharField(max_length=255, blank=True, null=True)
    titlenamee = models.CharField(max_length=255, blank=True, null=True)
    fnameeng = models.CharField(max_length=255, blank=True, null=True)
    lnameeng = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    religion = models.CharField(max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    dateofbirth = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    idcard = models.CharField(max_length=13, blank=True, null=True)
    othernationality = models.CharField(max_length=255, blank=True, null=True)
    idpassport = models.CharField(max_length=200, blank=True, null=True)
    pno = models.CharField(max_length=10, blank=True, null=True)
    pmoo = models.CharField(max_length=3, blank=True, null=True)
    pbul = models.CharField(max_length=50, blank=True, null=True)
    psoi = models.CharField(max_length=255, blank=True, null=True)
    proad = models.CharField(max_length=255, blank=True, null=True)
    psub = models.CharField(max_length=255, blank=True, null=True)
    pdir = models.CharField(max_length=255, blank=True, null=True)
    ppro = models.CharField(max_length=255, blank=True, null=True)
    ppost = models.CharField(max_length=5, blank=True, null=True)
    ptel = models.CharField(max_length=255, blank=True, null=True)
    pmobile = models.CharField(max_length=255, blank=True, null=True)
    pmail = models.CharField(max_length=255, blank=True, null=True)
    otheron = models.CharField(max_length=5, blank=True, null=True)
    othermoo = models.CharField(max_length=5, blank=True, null=True)
    otherbuilding = models.CharField(max_length=255, blank=True, null=True)
    othersoi = models.CharField(max_length=255, blank=True, null=True)
    otherroad = models.CharField(max_length=255, blank=True, null=True)
    othersub = models.CharField(max_length=255, blank=True, null=True)
    otherdir = models.CharField(max_length=255, blank=True, null=True)
    otherpro = models.CharField(max_length=255, blank=True, null=True)
    otherpost = models.CharField(max_length=5, blank=True, null=True)
    othertel = models.CharField(max_length=255, blank=True, null=True)
    facname = models.CharField(max_length=255, blank=True, null=True)
    facno = models.CharField(max_length=5, blank=True, null=True)
    facmoo = models.CharField(max_length=3, blank=True, null=True)
    facbul = models.CharField(max_length=255, blank=True, null=True)
    facsoi = models.CharField(max_length=255, blank=True, null=True)
    facroad = models.CharField(max_length=255, blank=True, null=True)
    facsub = models.CharField(max_length=255, blank=True, null=True)
    facdis = models.CharField(max_length=255, blank=True, null=True)
    facpro = models.CharField(max_length=255, blank=True, null=True)
    facpost = models.CharField(max_length=5, blank=True, null=True)
    factel = models.CharField(max_length=255, blank=True, null=True)
    facmobile = models.CharField(max_length=255, blank=True, null=True)
    q1801 = models.CharField(max_length=255, blank=True, null=True)
    q1802 = models.CharField(max_length=255, blank=True, null=True)
    q1803 = models.CharField(max_length=255, blank=True, null=True)
    q1804 = models.CharField(max_length=255, blank=True, null=True)
    q1805 = models.CharField(max_length=255, blank=True, null=True)
    swork = models.CharField(max_length=1, blank=True, null=True)
    sworkother = models.CharField(max_length=255, blank=True, null=True)
    q0901 = models.CharField(max_length=1, blank=True, null=True)
    q0902 = models.CharField(max_length=5, blank=True, null=True)
    q0903 = models.CharField(max_length=5, blank=True, null=True)
    q0904 = models.CharField(max_length=5, blank=True, null=True)
    q0905 = models.CharField(max_length=20, blank=True, null=True)
    q1001 = models.CharField(max_length=2, blank=True, null=True)
    q1002 = models.CharField(max_length=2, blank=True, null=True)
    q1003 = models.CharField(max_length=2, blank=True, null=True)
    q1004 = models.CharField(max_length=2, blank=True, null=True)
    q11bname = models.CharField(max_length=100, blank=True, null=True)
    q11bfac = models.CharField(max_length=150, blank=True, null=True)
    q11bmajor = models.CharField(max_length=100, blank=True, null=True)
    q11bdegree = models.CharField(max_length=50, blank=True, null=True)
    q11bgade = models.CharField(max_length=5, blank=True, null=True)
    q11mname = models.CharField(max_length=50, blank=True, null=True)
    q11mfac = models.CharField(max_length=50, blank=True, null=True)
    q11mmajor = models.CharField(max_length=50, blank=True, null=True)
    q11mdegree = models.CharField(max_length=50, blank=True, null=True)
    q11mgade = models.CharField(max_length=10, blank=True, null=True)
    q120101 = models.CharField(max_length=255, blank=True, null=True)
    q120102 = models.CharField(max_length=255, blank=True, null=True)
    q120103 = models.CharField(max_length=255, blank=True, null=True)
    q120201 = models.CharField(max_length=255, blank=True, null=True)
    q120202 = models.CharField(max_length=255, blank=True, null=True)
    q120203 = models.CharField(max_length=255, blank=True, null=True)
    q120301 = models.CharField(max_length=255, blank=True, null=True)
    q120302 = models.CharField(max_length=255, blank=True, null=True)
    q120303 = models.CharField(max_length=255, blank=True, null=True)
    q13 = models.CharField(max_length=255, blank=True, null=True)
    q1301pro = models.CharField(max_length=255, blank=True, null=True)
    q1301m = models.CharField(max_length=255, blank=True, null=True)
    q1301y = models.CharField(max_length=255, blank=True, null=True)
    q1301name = models.CharField(max_length=255, blank=True, null=True)
    q1301address = models.CharField(max_length=255, blank=True, null=True)
    q1301res = models.CharField(max_length=255, blank=True, null=True)
    q1302pro = models.CharField(max_length=255, blank=True, null=True)
    q1302ms = models.CharField(max_length=255, blank=True, null=True)
    q1302ys = models.CharField(max_length=255, blank=True, null=True)
    q1302me = models.CharField(max_length=255, blank=True, null=True)
    q1302ye = models.CharField(max_length=255, blank=True, null=True)
    q1302name = models.CharField(max_length=255, blank=True, null=True)
    q1302address = models.CharField(max_length=255, blank=True, null=True)
    q1302res = models.CharField(max_length=255, blank=True, null=True)
    q1401 = models.TextField(blank=True, null=True)
    q140201 = models.TextField(blank=True, null=True)
    q140202 = models.TextField(blank=True, null=True)
    q140203 = models.TextField(blank=True, null=True)
    q1403 = models.TextField(blank=True, null=True)
    q1404 = models.TextField(blank=True, null=True)
    dateadd = models.DateTimeField(blank=True, null=True)
    docinfac = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=6, blank=True, null=True)
    year = models.CharField(max_length=5, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    dadfname = models.CharField(max_length=100, blank=True, null=True)
    dadlname = models.CharField(max_length=100, blank=True, null=True)
    dadoccupation = models.CharField(max_length=100, blank=True, null=True)
    dadnameoffice = models.CharField(max_length=100, blank=True, null=True)
    dadposition = models.CharField(max_length=50, blank=True, null=True)
    dadtel = models.CharField(max_length=50, blank=True, null=True)
    dadaddress = models.CharField(max_length=200, blank=True, null=True)
    dademail = models.CharField(max_length=50, blank=True, null=True)
    momfname = models.CharField(max_length=100, blank=True, null=True)
    momlname = models.CharField(max_length=100, blank=True, null=True)
    momoccupation = models.CharField(max_length=100, blank=True, null=True)
    momnameoffice = models.CharField(max_length=150, blank=True, null=True)
    momposition = models.CharField(max_length=200, blank=True, null=True)
    momtel = models.CharField(max_length=20, blank=True, null=True)
    momaddress = models.CharField(max_length=200, blank=True, null=True)
    momemail = models.CharField(max_length=50, blank=True, null=True)
    picname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applyebmmaster'


class PrgApplyipen(models.Model):
    idapp = models.CharField(primary_key=True, max_length=10)
    titlenamet = models.CharField(max_length=255)
    fnameth = models.CharField(max_length=255)
    lnameth = models.CharField(max_length=255)
    titlenamee = models.CharField(max_length=255)
    fnameeng = models.CharField(max_length=255)
    lnameeng = models.CharField(max_length=255)
    dateofbirth = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    relgion = models.CharField(max_length=255)
    nationality = models.CharField(max_length=1)
    idcard = models.CharField(max_length=13)
    othernationality = models.CharField(max_length=255, blank=True, null=True)
    idpassport = models.CharField(max_length=255, blank=True, null=True)
    nopresent = models.CharField(max_length=255)
    moopresent = models.CharField(max_length=5)
    bulpresent = models.CharField(max_length=255, blank=True, null=True)
    soipresent = models.CharField(max_length=255, blank=True, null=True)
    roodpresent = models.CharField(max_length=255, blank=True, null=True)
    subpresent = models.CharField(max_length=255, blank=True, null=True)
    dispresent = models.CharField(max_length=255, blank=True, null=True)
    propresent = models.CharField(max_length=255, blank=True, null=True)
    postpresent = models.CharField(max_length=5, blank=True, null=True)
    telpresent = models.CharField(max_length=255, blank=True, null=True)
    mobilepresent = models.CharField(max_length=255, blank=True, null=True)
    otheron = models.CharField(max_length=10, blank=True, null=True)
    othermoo = models.CharField(max_length=5, blank=True, null=True)
    otherbuilding = models.CharField(max_length=255, blank=True, null=True)
    othersoi = models.CharField(max_length=255, blank=True, null=True)
    otherroad = models.CharField(max_length=255, blank=True, null=True)
    othersub = models.CharField(max_length=255, blank=True, null=True)
    otherdir = models.CharField(max_length=255, blank=True, null=True)
    otherpro = models.CharField(max_length=255, blank=True, null=True)
    otherpost = models.CharField(max_length=255, blank=True, null=True)
    othertel = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    dadfname = models.CharField(max_length=255, blank=True, null=True)
    dadlname = models.CharField(max_length=255, blank=True, null=True)
    dadoccupation = models.CharField(max_length=255, blank=True, null=True)
    dadnameoffice = models.CharField(max_length=255, blank=True, null=True)
    dadposition = models.CharField(max_length=255, blank=True, null=True)
    dadtel = models.CharField(max_length=255, blank=True, null=True)
    dadaddress = models.CharField(max_length=255, blank=True, null=True)
    dademail = models.CharField(max_length=255, blank=True, null=True)
    momfname = models.CharField(max_length=255, blank=True, null=True)
    momlname = models.CharField(max_length=255, blank=True, null=True)
    momoccupation = models.CharField(max_length=255, blank=True, null=True)
    momnameoffice = models.CharField(max_length=255, blank=True, null=True)
    momposition = models.CharField(max_length=255, blank=True, null=True)
    momtel = models.CharField(max_length=255, blank=True, null=True)
    momaddress = models.CharField(max_length=255, blank=True, null=True)
    momemail = models.CharField(max_length=255, blank=True, null=True)
    parentfname = models.CharField(max_length=255, blank=True, null=True)
    parentlname = models.CharField(max_length=255, blank=True, null=True)
    parentoccupation = models.CharField(max_length=255, blank=True, null=True)
    parentnameoffice = models.CharField(max_length=255, blank=True, null=True)
    parentposition = models.CharField(max_length=255, blank=True, null=True)
    parenttel = models.CharField(max_length=255, blank=True, null=True)
    parentaddress = models.CharField(max_length=255, blank=True, null=True)
    parentemail = models.CharField(max_length=255, blank=True, null=True)
    secondaryname = models.CharField(max_length=255, blank=True, null=True)
    secondaryprovince = models.CharField(max_length=255, blank=True, null=True)
    secondaryacademic = models.CharField(max_length=255, blank=True, null=True)
    secondarygrade = models.CharField(max_length=5, blank=True, null=True)
    secondarystart = models.CharField(max_length=255, blank=True, null=True)
    secondaryend = models.CharField(max_length=255, blank=True, null=True)
    hightschoolname = models.CharField(max_length=255, blank=True, null=True)
    hightschoolprovince = models.CharField(max_length=255, blank=True, null=True)
    hightschoolacademic = models.CharField(max_length=255, blank=True, null=True)
    hightschoolgrade = models.CharField(max_length=5, blank=True, null=True)
    hightschoolstart = models.CharField(max_length=255, blank=True, null=True)
    hightschoolend = models.CharField(max_length=255, blank=True, null=True)
    award = models.TextField(blank=True, null=True)
    q1301 = models.CharField(max_length=5, blank=True, null=True)
    q1302 = models.CharField(max_length=5, blank=True, null=True)
    q1303 = models.CharField(max_length=5, blank=True, null=True)
    q1304 = models.CharField(max_length=5, blank=True, null=True)
    q1304text = models.CharField(max_length=255, blank=True, null=True)
    q1305 = models.CharField(max_length=5, blank=True, null=True)
    q1305text = models.CharField(max_length=255, blank=True, null=True)
    q1306 = models.CharField(max_length=5, blank=True, null=True)
    q1306text = models.CharField(max_length=255, blank=True, null=True)
    q1307 = models.CharField(max_length=5, blank=True, null=True)
    q1307text = models.CharField(max_length=255, blank=True, null=True)
    q1308 = models.CharField(max_length=5, blank=True, null=True)
    q1308text = models.CharField(max_length=255, blank=True, null=True)
    q1401fac = models.CharField(max_length=255, blank=True, null=True)
    q1401name = models.CharField(max_length=255, blank=True, null=True)
    q1402fac = models.CharField(max_length=255, blank=True, null=True)
    q1402name = models.CharField(max_length=255, blank=True, null=True)
    q1403fac = models.CharField(max_length=255, blank=True, null=True)
    q1403name = models.CharField(max_length=255, blank=True, null=True)
    q1404fac = models.CharField(max_length=255, blank=True, null=True)
    q1404name = models.CharField(max_length=255, blank=True, null=True)
    q15 = models.TextField(blank=True, null=True)
    q1603 = models.CharField(max_length=5, blank=True, null=True)
    q1603gade = models.CharField(max_length=5, blank=True, null=True)
    q1604 = models.CharField(max_length=5, blank=True, null=True)
    q1605 = models.CharField(max_length=5, blank=True, null=True)
    q1606 = models.CharField(max_length=5, blank=True, null=True)
    q1607 = models.CharField(max_length=5, blank=True, null=True)
    q1608 = models.CharField(max_length=5, blank=True, null=True)
    q1609 = models.CharField(max_length=5, blank=True, null=True)
    q1610 = models.CharField(max_length=5, blank=True, null=True)
    q1611 = models.CharField(max_length=5, blank=True, null=True)
    q1612 = models.CharField(max_length=5, blank=True, null=True)
    q1613 = models.CharField(max_length=5, blank=True, null=True)
    q1614 = models.CharField(max_length=5, blank=True, null=True)
    q1615 = models.CharField(max_length=5, blank=True, null=True)
    q1616 = models.CharField(max_length=5, blank=True, null=True)
    dateadd = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    docinfac = models.DateTimeField(blank=True, null=True)
    picname = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applyipen'


class PrgApplyipenmaster(models.Model):
    idapp = models.CharField(primary_key=True, max_length=10)
    planstudy = models.CharField(max_length=1, blank=True, null=True)
    inmajor = models.CharField(max_length=1, blank=True, null=True)
    titlethesis = models.CharField(max_length=255, blank=True, null=True)
    titlenamet = models.CharField(max_length=10, blank=True, null=True)
    fnamet = models.CharField(max_length=255, blank=True, null=True)
    lnamet = models.CharField(max_length=255, blank=True, null=True)
    titlenamee = models.CharField(max_length=255, blank=True, null=True)
    fnamee = models.CharField(max_length=255, blank=True, null=True)
    lnamee = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    origin = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    birthday = models.CharField(max_length=20, blank=True, null=True)
    idcard = models.CharField(max_length=15, blank=True, null=True)
    pno = models.CharField(max_length=5, blank=True, null=True)
    pmoo = models.CharField(max_length=3, blank=True, null=True)
    pbul = models.CharField(max_length=50, blank=True, null=True)
    psoi = models.CharField(max_length=255, blank=True, null=True)
    proad = models.CharField(max_length=255, blank=True, null=True)
    psub = models.CharField(max_length=255, blank=True, null=True)
    pdir = models.CharField(max_length=255, blank=True, null=True)
    ppro = models.CharField(max_length=255, blank=True, null=True)
    ppost = models.CharField(max_length=5, blank=True, null=True)
    ptel = models.CharField(max_length=255, blank=True, null=True)
    pmobile = models.CharField(max_length=255, blank=True, null=True)
    pmail = models.CharField(max_length=255, blank=True, null=True)
    facname = models.CharField(max_length=255, blank=True, null=True)
    facno = models.CharField(max_length=5, blank=True, null=True)
    facmoo = models.CharField(max_length=3, blank=True, null=True)
    facbul = models.CharField(max_length=255, blank=True, null=True)
    facsoi = models.CharField(max_length=255, blank=True, null=True)
    facroad = models.CharField(max_length=255, blank=True, null=True)
    facsub = models.CharField(max_length=255, blank=True, null=True)
    facdis = models.CharField(max_length=255, blank=True, null=True)
    facpro = models.CharField(max_length=255, blank=True, null=True)
    facpost = models.CharField(max_length=5, blank=True, null=True)
    factel = models.CharField(max_length=255, blank=True, null=True)
    facmobile = models.CharField(max_length=255, blank=True, null=True)
    q1801 = models.CharField(max_length=255, blank=True, null=True)
    q1802 = models.CharField(max_length=255, blank=True, null=True)
    q1803 = models.CharField(max_length=255, blank=True, null=True)
    q1804 = models.CharField(max_length=255, blank=True, null=True)
    q1805 = models.CharField(max_length=255, blank=True, null=True)
    swork = models.CharField(max_length=1, blank=True, null=True)
    sworkother = models.CharField(max_length=255, blank=True, null=True)
    q0901 = models.CharField(max_length=1, blank=True, null=True)
    q0902 = models.CharField(max_length=5, blank=True, null=True)
    q0903 = models.CharField(max_length=5, blank=True, null=True)
    q0904 = models.CharField(max_length=5, blank=True, null=True)
    q0905 = models.CharField(max_length=5, blank=True, null=True)
    q1001 = models.CharField(max_length=2, blank=True, null=True)
    q1002 = models.CharField(max_length=2, blank=True, null=True)
    q1003 = models.CharField(max_length=2, blank=True, null=True)
    q1004 = models.CharField(max_length=2, blank=True, null=True)
    q11bname = models.CharField(max_length=255, blank=True, null=True)
    q11bfac = models.CharField(max_length=255, blank=True, null=True)
    q11bmajor = models.CharField(max_length=255, blank=True, null=True)
    q11bdegree = models.CharField(max_length=255, blank=True, null=True)
    q11mname = models.CharField(max_length=255, blank=True, null=True)
    q11mfac = models.CharField(max_length=255, blank=True, null=True)
    q11mmajor = models.CharField(max_length=255, blank=True, null=True)
    q11mdegree = models.CharField(max_length=255, blank=True, null=True)
    q120101 = models.CharField(max_length=255, blank=True, null=True)
    q120102 = models.CharField(max_length=255, blank=True, null=True)
    q120103 = models.CharField(max_length=255, blank=True, null=True)
    q120201 = models.CharField(max_length=255, blank=True, null=True)
    q120202 = models.CharField(max_length=255, blank=True, null=True)
    q120203 = models.CharField(max_length=255, blank=True, null=True)
    q120301 = models.CharField(max_length=255, blank=True, null=True)
    q120302 = models.CharField(max_length=255, blank=True, null=True)
    q120303 = models.CharField(max_length=255, blank=True, null=True)
    q1301pro = models.CharField(max_length=255, blank=True, null=True)
    q1301m = models.CharField(max_length=255, blank=True, null=True)
    q1301y = models.CharField(max_length=255, blank=True, null=True)
    q1301name = models.CharField(max_length=255, blank=True, null=True)
    q1301address = models.CharField(max_length=255, blank=True, null=True)
    q1301res = models.CharField(max_length=255, blank=True, null=True)
    q1302pro = models.CharField(max_length=255, blank=True, null=True)
    q1302ms = models.CharField(max_length=255, blank=True, null=True)
    q1302ys = models.CharField(max_length=255, blank=True, null=True)
    q1302me = models.CharField(max_length=255, blank=True, null=True)
    q1302ye = models.CharField(max_length=255, blank=True, null=True)
    q1302name = models.CharField(max_length=255, blank=True, null=True)
    q1302address = models.CharField(max_length=255, blank=True, null=True)
    q1302res = models.CharField(max_length=255, blank=True, null=True)
    q1401 = models.TextField(blank=True, null=True)
    q140201 = models.TextField(blank=True, null=True)
    q140202 = models.TextField(blank=True, null=True)
    q140203 = models.TextField(blank=True, null=True)
    q1403 = models.TextField(blank=True, null=True)
    q1404 = models.TextField(blank=True, null=True)
    dateadd = models.DateTimeField(blank=True, null=True)
    docinfac = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=6, blank=True, null=True)
    year = models.CharField(max_length=5, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applyipenmaster'


######### student_student #########


class StuEngrDegree(models.Model):
    id = models.IntegerField(primary_key=True)
    degree_name_th = models.CharField(max_length=30, blank=True, null=True)
    degree_name_en = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engr_degree'


class StuEngrDepartment(models.Model):
    depid = models.IntegerField(primary_key=True)
    major_th = models.CharField(max_length=100, blank=True, null=True)
    major_en = models.CharField(max_length=100, blank=True, null=True)
    department_th = models.CharField(max_length=100, blank=True, null=True)
    department_en = models.CharField(max_length=100, blank=True, null=True)
    dep_refer = models.CharField(max_length=3, blank=True, null=True)

    @property
    def context_data(self):
        return {
            'depid':self.depid,
            'major_th': self.major_th,
            'major_en': self.major_en,
            'department_th': self.department_th,
            'department_en': self.department_en,
            'dep_refer': self.dep_refer
        }
    
    class Meta:
        managed = False
        db_table = 'engr_department'


class StuEngrNation(models.Model):
    nation_id = models.IntegerField(primary_key=True)
    nation_th = models.CharField(max_length=10, blank=True, null=True)
    nation_en = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engr_nation'


class StuEngrProvince(models.Model):
    id = models.IntegerField(primary_key=True)
    province_name = models.CharField(max_length=100, blank=True, null=True)
    province_eng = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engr_province'


class StuEngrReligion(models.Model):
    religion_id = models.IntegerField(primary_key=True)
    religion_name_th = models.CharField(max_length=15, blank=True, null=True)
    religion_name_en = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engr_religion'


class StuEngrTitle(models.Model):
    id = models.IntegerField(primary_key=True)
    title_name_fth = models.CharField(max_length=30, blank=True, null=True)
    title_name_lth = models.CharField(max_length=20, blank=True, null=True)
    title_name_fen = models.CharField(max_length=30, blank=True, null=True)
    title_name_len = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engr_title'


class Memberebm(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    idcard = models.CharField(max_length=13)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    passwordedit = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memberebm'


class Province(models.Model):
    id = models.IntegerField(primary_key=True)
    province_name = models.CharField(max_length=100, blank=True, null=True)
    province_eng = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'


class StuStudent(models.Model):
    id = models.IntegerField(primary_key=True)
    stu_code = models.CharField(max_length=15, blank=True, null=True)
    title_id = models.CharField(max_length=3, blank=True, null=True)
    fname_th = models.CharField(max_length=255, blank=True, null=True)
    lname_th = models.CharField(max_length=255, blank=True, null=True)
    fname_en = models.CharField(max_length=255, blank=True, null=True)
    lname_en = models.CharField(max_length=255, blank=True, null=True)
    degree_id = models.CharField(max_length=1, blank=True, null=True)
    department_id = models.CharField(max_length=3, blank=True, null=True)
    advisor_id = models.CharField(max_length=10, blank=True, null=True)
    citizen_id = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.CharField(max_length=10, blank=True, null=True)
    religion_id = models.CharField(max_length=1, blank=True, null=True)
    nation_id = models.CharField(max_length=1, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    reg_address = models.CharField(max_length=255, blank=True, null=True)
    reg_road = models.CharField(max_length=255, blank=True, null=True)
    reg_subdistrict = models.CharField(max_length=255, blank=True, null=True)
    reg_amphur = models.CharField(max_length=255, blank=True, null=True)
    reg_province_id = models.CharField(max_length=2, blank=True, null=True)
    reg_telephone = models.CharField(max_length=15, blank=True, null=True)
    reg_postcode = models.CharField(max_length=5, blank=True, null=True)
    cur_address = models.CharField(max_length=255, blank=True, null=True)
    cur_road = models.CharField(max_length=255, blank=True, null=True)
    cur_subdistrict = models.CharField(max_length=255, blank=True, null=True)
    cur_amphur = models.CharField(max_length=255, blank=True, null=True)
    cur_province_id = models.CharField(max_length=2, blank=True, null=True)
    cur_postcode = models.CharField(max_length=5, blank=True, null=True)
    fat_fname = models.CharField(max_length=255, blank=True, null=True)
    fat_lname = models.CharField(max_length=255, blank=True, null=True)
    fat_year = models.CharField(max_length=3, blank=True, null=True)
    fat_address = models.CharField(max_length=255, blank=True, null=True)
    fat_road = models.CharField(max_length=255, blank=True, null=True)
    fat_subdistrict = models.CharField(max_length=255, blank=True, null=True)
    fat_amphur = models.CharField(max_length=255, blank=True, null=True)
    fat_province_id = models.CharField(max_length=2, blank=True, null=True)
    fat_postcode = models.CharField(max_length=5, blank=True, null=True)
    fat_telephone = models.CharField(max_length=30, blank=True, null=True)
    fat_occupation = models.CharField(max_length=150, blank=True, null=True)
    fat_position = models.CharField(max_length=150, blank=True, null=True)
    fat_status = models.CharField(max_length=2, blank=True, null=True)
    fat_type = models.CharField(max_length=255, blank=True, null=True)
    fat_salary = models.CharField(max_length=10, blank=True, null=True)
    fat_comname = models.CharField(max_length=255, blank=True, null=True)
    fat_compro = models.CharField(max_length=3, blank=True, null=True)
    fat_idcard = models.CharField(max_length=20, blank=True, null=True)
    mot_fname = models.CharField(max_length=255, blank=True, null=True)
    mot_lname = models.CharField(max_length=255, blank=True, null=True)
    mot_year = models.CharField(max_length=3, blank=True, null=True)
    mot_status = models.CharField(max_length=3, blank=True, null=True)
    mot_address = models.CharField(max_length=255, blank=True, null=True)
    mot_road = models.CharField(max_length=255, blank=True, null=True)
    mot_subdistrict = models.CharField(max_length=255, blank=True, null=True)
    mot_amphur = models.CharField(max_length=255, blank=True, null=True)
    mot_province_id = models.CharField(max_length=2, blank=True, null=True)
    mot_postcode = models.CharField(max_length=5, blank=True, null=True)
    mot_telephone = models.CharField(max_length=30, blank=True, null=True)
    mot_occupation = models.CharField(max_length=150, blank=True, null=True)
    mot_position = models.CharField(max_length=150, blank=True, null=True)
    mot_type = models.CharField(max_length=255, blank=True, null=True)
    mot_salary = models.CharField(max_length=10, blank=True, null=True)
    mot_comname = models.CharField(max_length=255, blank=True, null=True)
    mot_compro = models.CharField(max_length=3, blank=True, null=True)
    mot_idcard = models.CharField(max_length=20, blank=True, null=True)
    gus_fname = models.CharField(max_length=255, blank=True, null=True)
    gus_lname = models.CharField(max_length=255, blank=True, null=True)
    gus_relation = models.CharField(max_length=10, blank=True, null=True)
    gus_occupation = models.CharField(max_length=150, blank=True, null=True)
    gus_position = models.CharField(max_length=255, blank=True, null=True)
    gus_address = models.CharField(max_length=255, blank=True, null=True)
    gus_road = models.CharField(max_length=255, blank=True, null=True)
    gus_subdistrict = models.CharField(max_length=255, blank=True, null=True)
    gus_amphur = models.CharField(max_length=255, blank=True, null=True)
    gus_province_id = models.CharField(max_length=2, blank=True, null=True)
    gus_postcode = models.CharField(max_length=5, blank=True, null=True)
    gus_telephone = models.CharField(max_length=30, blank=True, null=True)
    con_fname = models.CharField(max_length=255, blank=True, null=True)
    con_lname = models.CharField(max_length=255, blank=True, null=True)
    con_address = models.CharField(max_length=255, blank=True, null=True)
    con_road = models.CharField(max_length=255, blank=True, null=True)
    con_subdistrict = models.CharField(max_length=255, blank=True, null=True)
    con_amphur = models.CharField(max_length=255, blank=True, null=True)
    con_province_id = models.CharField(max_length=2, blank=True, null=True)
    con_postcode = models.CharField(max_length=5, blank=True, null=True)
    con_telephone = models.CharField(max_length=30, blank=True, null=True)
    con_relation = models.CharField(max_length=30, blank=True, null=True)
    con_occupation = models.CharField(max_length=255, blank=True, null=True)
    con_position = models.CharField(max_length=255, blank=True, null=True)
    uppic = models.CharField(max_length=3, blank=True, null=True)
    sch_old = models.CharField(max_length=255, blank=True, null=True)
    sch_pro = models.CharField(max_length=100, blank=True, null=True)
    prinfo = models.CharField(max_length=10, blank=True, null=True)
    tuemail = models.CharField(max_length=50, blank=True, null=True)
    bankid = models.CharField(max_length=3, blank=True, null=True)
    bankno = models.CharField(max_length=20, blank=True, null=True)

    @property
    def context_data(self):
        return {
            'degree':self.degree_id,
            'std_code': self.stu_code,
            'fname_th': self.fname_th,
            'lname_th': self.lname_th,
            'fname_en': self.fname_en,
            'lname_en': self.lname_en,
            'advisor_id': self.advisor_id,
            'email': self.email,
            'title_id':self.title_id,
            'department_id':self.department_id

        }

    class Meta:
        managed = False
        db_table = 'stu_student'


class StuStudentOld(models.Model):
    id = models.IntegerField(primary_key=True)
    stu_code = models.CharField(max_length=15, blank=True, null=True)
    title_id = models.CharField(max_length=3, blank=True, null=True)
    fname_th = models.CharField(max_length=255, blank=True, null=True)
    lname_th = models.CharField(max_length=255, blank=True, null=True)
    fname_en = models.CharField(max_length=255, blank=True, null=True)
    lname_en = models.CharField(max_length=255, blank=True, null=True)
    degree_id = models.CharField(max_length=1, blank=True, null=True)
    department_id = models.CharField(max_length=3, blank=True, null=True)
    advisor_id = models.CharField(max_length=10, blank=True, null=True)
    citizen_id = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.CharField(max_length=10, blank=True, null=True)
    religion_id = models.CharField(max_length=1, blank=True, null=True)
    nation_id = models.CharField(max_length=1, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    reg_address = models.CharField(max_length=255, blank=True, null=True)
    reg_road = models.CharField(max_length=255, blank=True, null=True)
    reg_subdistrict = models.CharField(max_length=255, blank=True, null=True)
    reg_amphur = models.CharField(max_length=255, blank=True, null=True)
    reg_province_id = models.CharField(max_length=2, blank=True, null=True)
    reg_telephone = models.CharField(max_length=15, blank=True, null=True)
    reg_postcode = models.CharField(max_length=5, blank=True, null=True)
    cur_address = models.CharField(max_length=255, blank=True, null=True)
    cur_road = models.CharField(max_length=255, blank=True, null=True)
    cur_subdistrict = models.CharField(max_length=255, blank=True, null=True)
    cur_amphur = models.CharField(max_length=255, blank=True, null=True)
    cur_province_id = models.CharField(max_length=2, blank=True, null=True)
    cur_postcode = models.CharField(max_length=5, blank=True, null=True)
    fat_fname = models.CharField(max_length=255, blank=True, null=True)
    fat_lname = models.CharField(max_length=255, blank=True, null=True)
    fat_year = models.CharField(max_length=3, blank=True, null=True)
    fat_address = models.CharField(max_length=255, blank=True, null=True)
    fat_road = models.CharField(max_length=255, blank=True, null=True)
    fat_subdistrict = models.CharField(max_length=255, blank=True, null=True)
    fat_amphur = models.CharField(max_length=255, blank=True, null=True)
    fat_province_id = models.CharField(max_length=2, blank=True, null=True)
    fat_postcode = models.CharField(max_length=5, blank=True, null=True)
    fat_telephone = models.CharField(max_length=30, blank=True, null=True)
    fat_occupation = models.CharField(max_length=150, blank=True, null=True)
    fat_position = models.CharField(max_length=150, blank=True, null=True)
    fat_status = models.CharField(max_length=2, blank=True, null=True)
    fat_type = models.CharField(max_length=255, blank=True, null=True)
    fat_salary = models.CharField(max_length=10, blank=True, null=True)
    fat_comname = models.CharField(max_length=255, blank=True, null=True)
    fat_compro = models.CharField(max_length=3, blank=True, null=True)
    fat_idcard = models.CharField(max_length=20, blank=True, null=True)
    mot_fname = models.CharField(max_length=255, blank=True, null=True)
    mot_lname = models.CharField(max_length=255, blank=True, null=True)
    mot_year = models.CharField(max_length=3, blank=True, null=True)
    mot_status = models.CharField(max_length=3, blank=True, null=True)
    mot_address = models.CharField(max_length=255, blank=True, null=True)
    mot_road = models.CharField(max_length=255, blank=True, null=True)
    mot_subdistrict = models.CharField(max_length=255, blank=True, null=True)
    mot_amphur = models.CharField(max_length=255, blank=True, null=True)
    mot_province_id = models.CharField(max_length=2, blank=True, null=True)
    mot_postcode = models.CharField(max_length=5, blank=True, null=True)
    mot_telephone = models.CharField(max_length=30, blank=True, null=True)
    mot_occupation = models.CharField(max_length=150, blank=True, null=True)
    mot_position = models.CharField(max_length=150, blank=True, null=True)
    mot_type = models.CharField(max_length=255, blank=True, null=True)
    mot_salary = models.CharField(max_length=10, blank=True, null=True)
    mot_comname = models.CharField(max_length=255, blank=True, null=True)
    mot_compro = models.CharField(max_length=3, blank=True, null=True)
    mot_idcard = models.CharField(max_length=20, blank=True, null=True)
    gus_fname = models.CharField(max_length=255, blank=True, null=True)
    gus_lname = models.CharField(max_length=255, blank=True, null=True)
    gus_relation = models.CharField(max_length=10, blank=True, null=True)
    gus_occupation = models.CharField(max_length=150, blank=True, null=True)
    gus_position = models.CharField(max_length=255, blank=True, null=True)
    gus_address = models.CharField(max_length=255, blank=True, null=True)
    gus_road = models.CharField(max_length=255, blank=True, null=True)
    gus_subdistrict = models.CharField(max_length=255, blank=True, null=True)
    gus_amphur = models.CharField(max_length=255, blank=True, null=True)
    gus_province_id = models.CharField(max_length=2, blank=True, null=True)
    gus_postcode = models.CharField(max_length=5, blank=True, null=True)
    gus_telephone = models.CharField(max_length=30, blank=True, null=True)
    con_fname = models.CharField(max_length=255, blank=True, null=True)
    con_lname = models.CharField(max_length=255, blank=True, null=True)
    con_address = models.CharField(max_length=255, blank=True, null=True)
    con_road = models.CharField(max_length=255, blank=True, null=True)
    con_subdistrict = models.CharField(max_length=255, blank=True, null=True)
    con_amphur = models.CharField(max_length=255, blank=True, null=True)
    con_province_id = models.CharField(max_length=2, blank=True, null=True)
    con_postcode = models.CharField(max_length=5, blank=True, null=True)
    con_telephone = models.CharField(max_length=30, blank=True, null=True)
    con_relation = models.CharField(max_length=30, blank=True, null=True)
    con_occupation = models.CharField(max_length=255, blank=True, null=True)
    con_position = models.CharField(max_length=255, blank=True, null=True)
    uppic = models.CharField(max_length=3, blank=True, null=True)
    sch_old = models.CharField(max_length=255, blank=True, null=True)
    sch_pro = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stu_student_old'

