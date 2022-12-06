from django.urls import path
from . import views #importing from views.py file 

#importing the url path from views.py file 
urlpatterns = [

    path('', views.login),
    path('login/',views.login),
    path('mainpage/',views.mainpage),
    path('reports/',views.reports),
    path('criminalactivity/',views.criminalActivity),
    path('audits/',views.audits),
    path('cases/',views.cases),
]
