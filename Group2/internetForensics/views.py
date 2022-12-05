from django.shortcuts import render

"set Http Response for all the web pages available and to be accessed in the system"
from django.http import HttpResponse 


# Create your views here.
 
def login(request):
    return HttpResponse('Login page')

def dashboard(request):
    return HttpResponse('Dashboard page')
    
def reports(request): #report management
    return HttpResponse('Reports page')

def criminalActivity(request): #search and locate criminal activities
    return HttpResponse('Criminal Activity page')

def audits(request): #manage audits
    return HttpResponse('Audits page')   

def cases(request): #manage cases
    return HttpResponse('Cases page')