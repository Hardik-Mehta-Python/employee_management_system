from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department

# Create your views here.
def index(request):
    return render(request,"index.html")

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request,"all_emp.html",context)


def add_emp(request):
    return render(request,"add_emp.html")


def remove_emp(request):
    return render(request,"remove_emp.html")

def filter_emp(request):
    return render(request,"filter_emp.html")

