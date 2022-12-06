from django.shortcuts import render

"set Http Response for all the web pages available and to be accessed in the system"
from django.http import HttpResponse 


# Create your views here.
 
def login(request):
    return render(request, 'internetForensics/login.html')

def mainpage(request):
    return render(request, 'internetForensics/mainpage.html')
    
def reports(request): #report management
    return render(request, 'internetForensics/reports.html')

def criminalActivity(request): #search and locate criminal activities
    return render(request, 'internetForensics/criminalactivity.html')

def audits(request): #manage audits
    return render(request, 'internetForensics/audits.html')   

def cases(request): #manage cases
    return render(request, 'internetForensics/cases.html')