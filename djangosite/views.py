from django.shortcuts import render,redirect
from requests import request
from django.contrib.auth import logout

from .models import *
from .forms import *

# Create your views here.


def home(request):
    return render(request, 'djangosite/main.html')

def login_view(request):
    return render(request, 'djangosite/dassboard.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def signup(request):
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


def emp_delete(request, id):
    try:
        emp_obj = emp.objects.get(id = id)
        
        if emp_obj.user == request.user:
            emp_obj.delete()
            
    except Exception as e:
        print(e)
            
            
def emp_update(request, slug):
    context = {}
    try:
        emp_obj = emp.objects.get(slug = slug)
        
        if emp_obj.user != request.user:
            return redirect('/')
        
        initial_dict = {'content' : emp_obj.content}
        form = EmployeeForm(initial = initial_dict)
        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            name = request.POST.get('name')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
                
            emp_obj = EmployeeForm.objects.create(
                user = user , name = name, 
                content = content
            )
            
        context['emp_obj'] = emp_obj
        context['form'] = form
    except Exception  as e:
        print(e)
        
def search_emp(request):
    pass    
        
        

def verify(request, token):
    try:
        profile_obj = profile.objects.filter(token = token).first()
        
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')
    
    except Exception as e:
        print(e)