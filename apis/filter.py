import django_filters
from web.models import major as Major ,  StudentShowdetail3 , department as Department ,instructor as Instructor



class MajorFilter(django_filters.FilterSet):

    id = django_filters.CharFilter(method="filter_by_id")
    mname_th = django_filters.CharFilter(field_name="mname_th" , lookup_expr="icontains")
    mname_en = django_filters.CharFilter(field_name="mname_en" , lookup_expr="icontains")


    class Meta:
        model = Major
        fields = '__all__'

    def filter_by_id(self,queryset,name,value):
        ids = value.strip().split(",")
        return queryset.filter(id__in=ids)


class StudentShowdetail3Filter(django_filters.FilterSet):

    std_code = django_filters.CharFilter(field_name="std_code" , lookup_expr="icontains")
    tittle_name_lth = django_filters.CharFilter(field_name="tittle_name_lth" , lookup_expr="icontains")
    title_name_len = django_filters.CharFilter(field_name="title_name_len" , lookup_expr="icontains")
    fname_th = django_filters.CharFilter(field_name="fname_th" , lookup_expr="icontains")
    lname_th = django_filters.CharFilter(field_name="lname_th" , lookup_expr="icontains")   
    fname_en = django_filters.CharFilter(field_name="fname_en" , lookup_expr="icontains")
    lname_en = django_filters.CharFilter(field_name="lname_en" , lookup_expr="icontains")   
    major_th = django_filters.CharFilter(field_name="major_th" , lookup_expr="icontains")
    major_en = django_filters.CharFilter(field_name="major_en" , lookup_expr="icontains")   
    department_th = django_filters.CharFilter(field_name="department_th" , lookup_expr="icontains")
    department_en = django_filters.CharFilter(field_name="department_en" , lookup_expr="icontains")   
    advisor_id = django_filters.CharFilter(field_name="advisor_id" , lookup_expr="icontains")
    email = django_filters.CharFilter(field_name="email" , lookup_expr="icontains")

    class Meta:
        model = StudentShowdetail3
        fields = '__all__'

    # def filter_by_task_id(self,queryset,name,value):
    #     task_ids = value.strip().split(",")
    #     return queryset.filter(id__in=task_ids)


class DepartmentFilter(django_filters.FilterSet):

    id = django_filters.CharFilter(method="filter_by_id")
    dname_th = django_filters.CharFilter(field_name="dname_th" , lookup_expr="icontains")
    dname_en = django_filters.CharFilter(field_name="dname_en" , lookup_expr="icontains")


    class Meta:
        model = Department
        fields = '__all__'

    def filter_by_id(self,queryset,name,value):
        ids = value.strip().split(",")
        return queryset.filter(id__in=ids)


class InstructorFilter(django_filters.FilterSet):

    id = django_filters.CharFilter(method="filter_by_id")
    fname_th = django_filters.CharFilter(field_name="fname_th" , lookup_expr="icontains")
    lname_th = django_filters.CharFilter(field_name="lname_th" , lookup_expr="icontains")
    fname_en = django_filters.CharFilter(field_name="fname_en" , lookup_expr="icontains")
    lname_en = django_filters.CharFilter(field_name="lname_en" , lookup_expr="icontains")
    department = django_filters.CharFilter(field_name="department" , lookup_expr="icontains")
    email = django_filters.CharFilter(field_name="email" , lookup_expr="icontains")

    class Meta:
        model = Instructor
        fields = '__all__'

    def filter_by_id(self,queryset,name,value):
        ids = value.strip().split(",")
        return queryset.filter(id__in=ids)