from django.shortcuts import render, redirect
from staff.views import staff_authenticated
from .models import doctor, Patient, ReportType

def get_doctor_details(doctor_id=None):
    if doctor_id is None:
        get_doctor = doctor.objects.all().order_by('-id')
    else:
        get_doctor = doctor.objects.get(id=doctor_id)
    return get_doctor

def get_patient_details(patient_id=None):
    if patient_id is None:
        get_patient = Patient.objects.all().order_by('-id')
    else:
        get_patient = Patient.objects.get(id=patient_id)
    return get_patient

def get_report_details(report_type_id=None):
    if report_type_id is None:
        get_report = ReportType.objects.all().order_by('-id')
    else:
        get_report = ReportType.objects.get(id=report_type_id)
    return get_report

@staff_authenticated
def dashboard_view(request):
    context = {
        'total_doctors':get_doctor_details().count(),
        'total_patients':get_patient_details().count()
    }
    return render(request, 'dashboard.html', context)

@staff_authenticated
def doctors_view(request):
    context = {
        'doctors':get_doctor_details()
    }
    return render(request, 'doctors.html', context)

@staff_authenticated
def patients_view(request):
    if request.method == 'POST':
        first_name_ = request.POST['firstname']
        last_name_ = request.POST['lastname']
        mobile_ = request.POST['mobile']
        doctor_id_ = request.POST['doctor']
        report_type_id_ = request.POST['report_type']
        paid_payment_ = request.POST['payment']
        address_ = request.POST['address']

        new_patient = Patient.objects.create(
            first_name=first_name_,
            last_name=last_name_,
            mobile=mobile_,
            doctor_id_id=doctor_id_,
            report_type_id = report_type_id_,
            paid_payment=paid_payment_,
            address=address_
        )
        new_patient.save()
        print('Patient addedd')
        return redirect('patients_view')
    context = {
        'doctors':get_doctor_details(),
        'reports':get_report_details(),
        'patients':get_patient_details()
    }
    return render(request, 'patients.html',context)

@staff_authenticated
def patient_delete(request, patient_id):
    print(patient_id)
    get_patient = get_patient_details(patient_id=patient_id)
    get_patient.delete()
    print('patient deleted')
    return redirect('patients_view')