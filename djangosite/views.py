from django.shortcuts import render
from requests import request

# Create your views here.


def home(request):
    return render(request, 'main.html')

def add_emp(request):
    return render(request, 'add_emp.html')
