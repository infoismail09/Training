from django.shortcuts import render
from .models import Employee,ExcelFile
import pandas as pd
from django.http import JsonResponse
from django.conf import settings
# Create your views here.


def export_data_to_excel(request):
    objs = Employee.objects.all()
    data = []

    for obj in objs:
        data.append({
            "employee_name":obj.employee_name,
            "employee_contact":obj.employee_contact,
            "employee_address":obj.employee_address
        })
    pd.DataFrame(data).to_excel('output.xlsx')
    return JsonResponse({
        'status':200
    })


def import_data_to_db(request):
    if request.method == 'POST':
        file = request.FILES['files']
        obj = ExcelFile.objects.create(
            file = file
        )
        path = file.file
        print(f'{settings.BASE_DIR}/{path}')
        df = pd.read_excel(path)
        print(df)
        
    return render(request, 'excel.html')