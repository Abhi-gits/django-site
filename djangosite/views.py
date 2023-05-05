from django.shortcuts import render,redirect
from requests import request

from .models import *
from .forms import *

# Create your views here.


def home(request):
    return render(request, 'djangosite/main.html')

def add_emp(request):
    employee = emp.objects.all()
    
    form = EmployeeForm()
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('djangosite/add_emp.html')    
    context = {'employees': employee, 'form': form}
    return render(request, 'djangosite/add_emp.html', context)
