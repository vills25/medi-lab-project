from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard_view/', dashboard_view, name='dashboard_view'),
    path('doctors_view/', doctors_view, name='doctors_view'),
    path('add_doctor_view/', add_doctor_view, name='add_doctor_view'),
    path('patients_view/', patients_view, name='patients_view'),
    path('patient_delete/<int:patient_id>', patient_delete, name='patient_delete'),
    path('patient_update/<int:patient_id>', patient_update, name='patient_update'),
    path('doctor_edit_view/<int:doctor_id>', doctor_edit_view, name='doctor_edit_view'),
    path('patient_account/<int:patient_id>', patient_account, name='patient_account'),
    path('tasks_view/', tasks_view, name='tasks_view'),
]
    

# Create your URLS here.