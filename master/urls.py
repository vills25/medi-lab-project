from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard_view/', dashboard_view, name='dashboard_view'),
    path('doctors_view/', doctors_view, name='doctors_view'),
    path('patients_view/', patients_view, name='patients_view'),
    
    ]

# Create your URLS here.