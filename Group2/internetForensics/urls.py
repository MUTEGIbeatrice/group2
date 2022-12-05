from django.urls import path
from . import views #importing from views.py file 

#importing the url path (html responses) from views.py file 
urlpatterns = [

    path('', views.login),
    path('login/',views.login),
    path('dashboard/',views.dashboard),
    path('reports/',views.reports),
    path('criminalactivity/',views.criminalActivity),
    path('audits/',views.audits),
    path('cases/',views.cases),
]
