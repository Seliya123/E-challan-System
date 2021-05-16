from django.urls import path
from django.contrib.auth import views

from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('finedetails/',views.finedetails, name='finedetails'),
    path('challan/',views.challan, name='challan'),
    path('logins/',views.logins, name='logins'),
    path('logout/', views.logouts, name = 'logout'),
     path('records/', views.records, name = 'records'),
    
  
    
]