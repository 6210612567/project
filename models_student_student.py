# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addnewstudent(models.Model):
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


class Applyebm(models.Model):
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


class Applyebmmaster(models.Model):
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


class Applyipen(models.Model):
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


class Applyipenmaster(models.Model):
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


class Bank(models.Model):
    id = models.IntegerField()
    bankname = models.CharField(max_length=200, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank'


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


class EngrDegree(models.Model):
    id = models.IntegerField(primary_key=True)
    degree_name_th = models.CharField(max_length=30, blank=True, null=True)
    degree_name_en = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engr_degree'


class EngrDepartment(models.Model):
    depid = models.IntegerField(primary_key=True)
    major_th = models.CharField(max_length=100, blank=True, null=True)
    major_en = models.CharField(max_length=100, blank=True, null=True)
    department_th = models.CharField(max_length=100, blank=True, null=True)
    department_en = models.CharField(max_length=100, blank=True, null=True)
    dep_refer = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engr_department'


class EngrNation(models.Model):
    nation_id = models.IntegerField(primary_key=True)
    nation_th = models.CharField(max_length=10, blank=True, null=True)
    nation_en = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engr_nation'


class EngrProvince(models.Model):
    id = models.IntegerField(primary_key=True)
    province_name = models.CharField(max_length=100, blank=True, null=True)
    province_eng = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engr_province'


class EngrReligion(models.Model):
    religion_id = models.IntegerField(primary_key=True)
    religion_name_th = models.CharField(max_length=15, blank=True, null=True)
    religion_name_en = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engr_religion'


class EngrTitle(models.Model):
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
