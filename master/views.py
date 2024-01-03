from django.shortcuts import render
from staff.views import staff_authenticated

@staff_authenticated
def dashboard_view(request):
    return render(request, 'dashboard.html')

@staff_authenticated
def doctors_view(request):
    return render(request, 'doctors.html')

@staff_authenticated
def patients_view(request):
    return render(request, 'patients.html')


# Create your views here.
