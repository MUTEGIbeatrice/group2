from django.urls import path
from . import views #importing from views.py file 

#importing the url path (html responses) from views.py file 
urlpatterns = [

    path('', views.home),
    path('register/',views.register),
    path('dashboard/',views.dashboard),
    path('reports/',views.reports),
    path('criminalactivity/',views.criminalActivity),
    path('audits/',views.audits),
    path('cases/',views.cases),
]
