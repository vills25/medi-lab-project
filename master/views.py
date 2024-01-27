from django.shortcuts import render, redirect
from django.utils import timezone
from staff.views import staff_authenticated
from .models import doctor, Patient, ReportType, paid_installment
from datetime import timedelta
import humanize

current_time = timezone.now()



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
def add_doctor_view(request):

    if request.method == 'POST':
        name_ = request.POST['name']
        degree_ = request.POST['degree']
        contact_ = request.POST['contact']
        summary_ = request.POST['summary']
        address_ = request.POST['address']

        new_doctor = doctor.objects.create(
            name=name_,
            degree=degree_,
            contact=contact_,
            summary=summary_,
            address=address_
        )
        new_doctor.save()
        print('doctor addedd')
        return redirect('doctors_view')
    return render(request, 'add-doctors.html')

#  @staff_authenticated
# def doctor_edit_view(request, doctor_id):
#     get_doctor = get_doctor_details(doctor_id=doctor_id)
#     if request.method == 'POST':
#         name_ = request.POST['name']
#         degree_ = request.POST['degree']
#         contact_ = request.POST['contact']
#         summary_ = request.POST['summary']
#         address_ = request.POST['address']

#         get_doctor.name=name_,
#         get_doctor.degree=degree_,
#         get_doctor.contact=contact_,
#         get_doctor.summary=summary_,
#         get_doctor.address=address_

#         get_doctor.save()
#         print("Doctor data updated")
#         return redirect('doctors_view')
       
#     context = {
#         'doctors':get_doctor_details(),
#     }
#     return render(request, 'edit-doctors.html', context)

@staff_authenticated
def doctor_edit_view(request, doctor_id):
    get_doctor = get_doctor_details(doctor_id=doctor_id)
    if request.method == 'POST':
        name_ = request.POST['name']
        degree_ = request.POST['degree']
        contact_ = request.POST['contact']
        summary_ = request.POST['summary']
        address_ = request.POST['address']

        update_result = update_doctor_data(doctor_id, name_, degree_, contact_, summary_, address_)

        if update_result:
            print("Doctor data updated")
            return redirect('doctors_view')
        else:
            print("Failed to update doctor data")
            # Handle the case where the doctor was not found or other errors
            # You might want to render an error message or redirect to an error page
       
    context = {
        'doctors': get_doctor_details(),
    }
    return render(request, 'edit-doctors.html', context)

def update_doctor_data(doctor_id, name, degree, contact, summary, address):
    try:
        doctor_instance = doctor.objects.get(id=doctor_id)
        doctor_instance.name = name
        doctor_instance.degree = degree
        doctor_instance.contact = contact
        doctor_instance.summary = summary
        doctor_instance.address = address
        doctor_instance.save()
        print("Doctor data updated successfully")
        return True
    except doctor.DoesNotExist:
        print("Doctor not found")
        return False

@staff_authenticated
def patients_view(request):
    today_patients = Patient.objects.filter(created_at__date=current_time.date())

    if request.method == 'POST':
        first_name_ = request.POST['firstname']
        last_name_ = request.POST['lastname']
        mobile_ = request.POST['mobile']
        doctor_id_ = request.POST['doctor']
        report_type_id_ = request.POST['report_type']
        address_ = request.POST['address']

        new_patient = Patient.objects.create(
            first_name=first_name_,
            last_name=last_name_,
            mobile=mobile_,
            doctor_id_id=doctor_id_,
            report_type_id = report_type_id_,
            address=address_
        )
        new_patient.save()
        print('Patient addedd')
        return redirect('patients_view')
    context = {
        'doctors':get_doctor_details(),
        'reports':get_report_details(),
        'patients':get_patient_details(),
        'today_patients':today_patients,
        'current_time': current_time.date(),
        'humanize': humanize.naturalday(current_time)
    }
    return render(request, 'patients.html',context)

@staff_authenticated
def patient_update(request, patient_id):
    get_patient = get_patient_details(patient_id=patient_id)
    if request.method == 'POST':
        first_name_ = request.POST['firstname']
        last_name_ = request.POST['lastname']
        mobile_ = request.POST['mobile']
        doctor_id_ = request.POST['doctor']
        report_type_id_ = request.POST['report_type']
        address_ = request.POST['address']

        get_patient.first_name = first_name_
        get_patient.last_name = last_name_
        get_patient.mobile = mobile_
        get_patient.doctor_id_id = doctor_id_
        get_patient.report_type_id = report_type_id_
        get_patient.address = address_
        get_patient.save()
        print("Patient data updated")
        return redirect('patients_view')
      
    context = {
        'patient':get_patient,
        'doctors':get_doctor_details(),
        'reports':get_report_details(),
        'humanize': humanize.naturalday(current_time - get_patient.created_at)
    }
    return render(request, 'patient-edit.html', context)

@staff_authenticated
def patient_account(request, patient_id):
    get_patient = get_patient_details(patient_id=patient_id)
    payment_entries = paid_installment.objects.filter(patient_id=patient_id)

    if request.method == "POST":
        payment_installment_ = float(request.POST['payment_installment'])

        if payment_installment_ != 0:
            if payment_installment_ <= get_patient.remaining_amount:
                get_patient.paid_amount += payment_installment_
                get_patient.remaining_amount -= payment_installment_

                if get_patient.total_amount == get_patient.paid_amount:
                    get_patient.payment_status = 'Done'
                else:
                    get_patient.payment_status = 'Partially'      
                get_patient.save()

                new_payment_entry = paid_installment.objects.create(
                    patient_id_id = patient_id,
                    paid_payment = payment_installment_
                )
                new_payment_entry.save()
                print("payment added")
                return redirect('patient_account', patient_id=patient_id)
            else:
                print("Payment installment must be small than remaining amount")
                return redirect('patient_account', patient_id=patient_id)
        else:
            print("You can not add 0")
            return redirect('patient_account', patient_id=patient_id)

    context = {
        'patient':get_patient,
        'entreis':payment_entries
    }
    return render(request, 'patient-account.html', context)

@staff_authenticated
def patient_delete(request, patient_id):
    get_patient = get_patient_details(patient_id=patient_id)
    get_patient.delete()
    print('patient deleted')
    return redirect('patients_view')

