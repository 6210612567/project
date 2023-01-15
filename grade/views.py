from django.shortcuts import render
import json
import pandas as pd
from .models import CustomGradeField,Grade
# def handle_uploaded_file(f):
#     with open('path/to/save/file', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

# Create your views here.
def index(request):
    if request.method == 'POST':
        try:
            df = pd.read_excel(request.FILES['file'])
            data = df.to_json(orient='records')
            student_list = json.loads(data)
            # print(json_str)
            # json_str = [{"aa":11,"bb":22,"cc":33,"dd":44},{"aa":"\u0e01\u0e01","bb":"\u0e02\u0e02","cc":"\u0e04\u0e04","dd":"\u0e07\u0e07"}]
            table_key = ['name','subject','grade','midterm','final']
            for student in student_list:
                student_data = {}
                custom_obj_list = []
                for key in student:
                    if key in table_key:
                        student_data[key] = student[key]
                    else:
                        custom_obj = CustomGradeField.objects.create(name=key,value=student[key])
                        custom_obj_list.append(custom_obj)
                grade_obj = Grade.objects.create(name=student['name'],subject=student['subject'],grade=student['grade'],midterm=student['midterm'],final=student['final'])
                for custom_field in custom_obj_list:
                    grade_obj.customfield.add(custom_field)
                    grade_obj.save()   
            ### save data to excel 
            # df = pd.DataFrame(student_list)
            # df.to_excel("output.xlsx", index=False)
            return render(request, "grade/index.html")
        except Exception as e:
            print('File error',e)
        return render(request, "grade/index.html")
    else:
        # subject = 'cn203'
        subject_list = Grade.objects.values_list('subject', flat=True).distinct()
        output = []
        for subject in subject_list:
            grade_list = Grade.objects.filter(subject=subject)
            header_list = ['name','subject','grade','midterm','final']
            for grade in grade_list:
                for custom_field in grade.customfield.all():
                    header_list.append(custom_field.name)
                break
            output.append({'grade_list':grade_list,'header_list':header_list})
        return render(request, "grade/index.html",{'output':output})





