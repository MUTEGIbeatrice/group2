from django.shortcuts import render

"set Http Response for all the web pages available and to be accessed in the system"
from django.http import HttpResponse 


# Create your views here.
 
def home(request):
    return HttpResponse('Home page')
    
def register(request):
    return HttpResponse('Registration page')

def dashboard(request):
    return HttpResponse('Dashboard page')
    
def reports(request):
    return HttpResponse('Reports page')

def criminalActivity(request):
    return HttpResponse('Criminal Activity page')

def audits(request):
    return HttpResponse('Audits page')   

def cases(request):
    return HttpResponse('Cases page')