import django_filters
# import student models
from apis.models import StuStudent,StuEngrDepartment
# import prg_human models
from apis.models import PrgEngrDepartment,PrgPerPerson

# class MajorFilter(django_filters.FilterSet):

#     id = django_filters.CharFilter(method="filter_by_id")
#     mname_th = django_filters.CharFilter(field_name="mname_th" , lookup_expr="icontains")
#     mname_en = django_filters.CharFilter(field_name="mname_en" , lookup_expr="icontains")


#     class Meta:
#         model = Major
#         fields = '__all__'

#     def filter_by_id(self,queryset,name,value):
#         ids = value.strip().split(",")
#         return queryset.filter(id__in=ids)


class StuStudentFilter(django_filters.FilterSet): 
    id = django_filters.CharFilter(method="filter_by_id")
    stu_code = django_filters.CharFilter( lookup_expr="icontains")
    title_id = django_filters.CharFilter(field_name="title_id" , lookup_expr="icontains")
    fname_th = django_filters.CharFilter(field_name="fname_th" , lookup_expr="icontains")
    lname_th = django_filters.CharFilter(field_name="lname_th" , lookup_expr="icontains")
    fname_en = django_filters.CharFilter(field_name="fname_en" , lookup_expr="icontains")
    lname_en = django_filters.CharFilter(field_name="lname_en" , lookup_expr="icontains")
    degree_id = django_filters.CharFilter(field_name="degree_id" , lookup_expr="icontains")
    department_id = django_filters.CharFilter(field_name="department_id" , lookup_expr="icontains")
    advisor_id = django_filters.CharFilter(field_name="advisor_id" , lookup_expr="icontains")
    citizen_id = django_filters.CharFilter(field_name="citizen_id" , lookup_expr="icontains")
    birthdate = django_filters.CharFilter(field_name="birthdate" , lookup_expr="icontains")
    religion_id = django_filters.CharFilter(field_name="religion_id" , lookup_expr="icontains")
    nation_id = django_filters.CharFilter(field_name="nation_id" , lookup_expr="icontains")
    sex = django_filters.CharFilter(field_name="sex" , lookup_expr="icontains")
    nickname = django_filters.CharFilter( lookup_expr="icontains")
    email = django_filters.CharFilter( lookup_expr="icontains")
    reg_address = django_filters.CharFilter( lookup_expr="icontains")
    reg_road = django_filters.CharFilter( lookup_expr="icontains")
    reg_subdistrict = django_filters.CharFilter( lookup_expr="icontains")
    reg_amphur = django_filters.CharFilter( lookup_expr="icontains")
    reg_province_id = django_filters.CharFilter( lookup_expr="icontains")
    reg_telephone = django_filters.CharFilter( lookup_expr="icontains")
    reg_postcode = django_filters.CharFilter( lookup_expr="icontains")
    cur_address = django_filters.CharFilter( lookup_expr="icontains")
    cur_road = django_filters.CharFilter( lookup_expr="icontains")
    cur_subdistrict = django_filters.CharFilter( lookup_expr="icontains")
    cur_amphur = django_filters.CharFilter( lookup_expr="icontains")
    cur_province_id = django_filters.CharFilter( lookup_expr="icontains")
    cur_postcode = django_filters.CharFilter( lookup_expr="icontains")
    fat_fname = django_filters.CharFilter( lookup_expr="icontains")
    fat_lname = django_filters.CharFilter( lookup_expr="icontains")
    fat_year = django_filters.CharFilter( lookup_expr="icontains")
    fat_address = django_filters.CharFilter( lookup_expr="icontains")
    fat_road = django_filters.CharFilter( lookup_expr="icontains")
    fat_subdistrict = django_filters.CharFilter( lookup_expr="icontains")
    fat_amphur = django_filters.CharFilter( lookup_expr="icontains")
    fat_province_id = django_filters.CharFilter( lookup_expr="icontains")
    fat_postcode = django_filters.CharFilter( lookup_expr="icontains")
    fat_telephone = django_filters.CharFilter( lookup_expr="icontains")
    fat_occupation = django_filters.CharFilter( lookup_expr="icontains")
    fat_position = django_filters.CharFilter( lookup_expr="icontains")
    fat_status = django_filters.CharFilter( lookup_expr="icontains")
    fat_type = django_filters.CharFilter( lookup_expr="icontains")
    fat_salary = django_filters.CharFilter( lookup_expr="icontains")
    fat_comname = django_filters.CharFilter( lookup_expr="icontains")
    fat_compro = django_filters.CharFilter( lookup_expr="icontains")
    fat_idcard = django_filters.CharFilter( lookup_expr="icontains")
    mot_fname = django_filters.CharFilter( lookup_expr="icontains")
    mot_lname = django_filters.CharFilter( lookup_expr="icontains")
    mot_year = django_filters.CharFilter( lookup_expr="icontains")
    mot_status = django_filters.CharFilter( lookup_expr="icontains")
    mot_address = django_filters.CharFilter( lookup_expr="icontains")
    mot_road = django_filters.CharFilter( lookup_expr="icontains")
    mot_subdistrict = django_filters.CharFilter( lookup_expr="icontains")
    mot_amphur = django_filters.CharFilter( lookup_expr="icontains")
    mot_province_id = django_filters.CharFilter( lookup_expr="icontains")
    mot_postcode = django_filters.CharFilter( lookup_expr="icontains")
    mot_telephone = django_filters.CharFilter( lookup_expr="icontains")
    mot_occupation = django_filters.CharFilter( lookup_expr="icontains")
    mot_position = django_filters.CharFilter( lookup_expr="icontains")
    mot_type = django_filters.CharFilter( lookup_expr="icontains")
    mot_salary = django_filters.CharFilter( lookup_expr="icontains")
    mot_comname = django_filters.CharFilter( lookup_expr="icontains")
    mot_compro = django_filters.CharFilter( lookup_expr="icontains")
    mot_idcard = django_filters.CharFilter( lookup_expr="icontains")
    gus_fname = django_filters.CharFilter( lookup_expr="icontains")
    gus_lname = django_filters.CharFilter( lookup_expr="icontains")
    gus_relation = django_filters.CharFilter( lookup_expr="icontains")
    gus_occupation = django_filters.CharFilter( lookup_expr="icontains")
    gus_position = django_filters.CharFilter( lookup_expr="icontains")
    gus_address = django_filters.CharFilter( lookup_expr="icontains")
    gus_road = django_filters.CharFilter( lookup_expr="icontains")
    gus_subdistrict = django_filters.CharFilter( lookup_expr="icontains")
    gus_amphur = django_filters.CharFilter( lookup_expr="icontains")
    gus_province_id = django_filters.CharFilter( lookup_expr="icontains")
    gus_postcode = django_filters.CharFilter( lookup_expr="icontains")
    gus_telephone = django_filters.CharFilter( lookup_expr="icontains")
    con_fname = django_filters.CharFilter( lookup_expr="icontains")
    con_lname = django_filters.CharFilter( lookup_expr="icontains")
    con_address = django_filters.CharFilter( lookup_expr="icontains")
    con_road = django_filters.CharFilter( lookup_expr="icontains")
    con_subdistrict = django_filters.CharFilter( lookup_expr="icontains")
    con_amphur = django_filters.CharFilter( lookup_expr="icontains")
    con_province_id = django_filters.CharFilter( lookup_expr="icontains")
    con_postcode = django_filters.CharFilter( lookup_expr="icontains")
    con_telephone = django_filters.CharFilter( lookup_expr="icontains")
    con_relation = django_filters.CharFilter( lookup_expr="icontains")
    con_occupation = django_filters.CharFilter( lookup_expr="icontains")
    con_position = django_filters.CharFilter( lookup_expr="icontains")
    uppic = django_filters.CharFilter( lookup_expr="icontains")
    sch_old = django_filters.CharFilter( lookup_expr="icontains")
    sch_pro = django_filters.CharFilter( lookup_expr="icontains")
    prinfo = django_filters.CharFilter( lookup_expr="icontains")
    tuemail = django_filters.CharFilter( lookup_expr="icontains")
    bankid = django_filters.CharFilter( lookup_expr="icontains")
    bankno = django_filters.CharFilter( lookup_expr="icontains")

    def filter_by_id(self,queryset,name,value):
        ids = value.strip().split(",")
        return queryset.filter(id__in=ids)
    
    class Meta:
        model = StuStudent
        fields = '__all__'

    # def filter_by_task_id(self,queryset,name,value):
    #     task_ids = value.strip().split(",")
    #     return queryset.filter(id__in=task_ids)


class DepartmentFilter(django_filters.FilterSet):

    depid = django_filters.CharFilter(method="filter_by_id")
    major_th = django_filters.CharFilter( lookup_expr="icontains")
    major_en = django_filters.CharFilter( lookup_expr="icontains")
    department_th = django_filters.CharFilter( lookup_expr="icontains")
    department_en = django_filters.CharFilter( lookup_expr="icontains")
    dep_refer = django_filters.CharFilter( lookup_expr="icontains")


    class Meta:
        model = StuEngrDepartment
        fields = '__all__'

    def filter_by_id(self,queryset,name,value):
        ids = value.strip().split(",")
        return queryset.filter(depid__in=ids)


class InstructorDepartmentFilter(django_filters.FilterSet):
    departmentid = django_filters.CharFilter(method="filter_by_id")
    departmentname = django_filters.CharFilter( lookup_expr="icontains")

    class Meta:
        model = PrgEngrDepartment
        fields = '__all__'

    def filter_by_id(self,queryset,name,value):
        ids = value.strip().split(",")
        return queryset.filter(departmentid__in=ids)
    

class InstructorFilter(django_filters.FilterSet):

    personid = django_filters.CharFilter(method="filter_by_id")
    title = django_filters.CharFilter( lookup_expr="icontains")
    fname_t = django_filters.CharFilter( lookup_expr="icontains")
    lname_t = django_filters.CharFilter( lookup_expr="icontains")
    fname_e = django_filters.CharFilter( lookup_expr="icontains")
    lname_e = django_filters.CharFilter( lookup_expr="icontains")
    department = django_filters.CharFilter( lookup_expr="icontains")
    title_academic = django_filters.CharFilter( lookup_expr="icontains")
    ad_user = django_filters.CharFilter( lookup_expr="icontains")
    full_ad = django_filters.CharFilter( lookup_expr="icontains")


    class Meta:
        model = PrgPerPerson
        fields = '__all__'

    def filter_by_id(self,queryset,name,value):
        ids = value.strip().split(",")
        return queryset.filter(personid__in=ids)