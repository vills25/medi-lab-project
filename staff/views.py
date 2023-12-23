from django.shortcuts import render
from .models import StaffRegister

def login_view(request):
    if request.method == 'POST':
        login_id_ = request.POST['login_id']
        password_ = request.POST['password']
        try:
            print(login_id_, password_)
            get_staff = StaffRegister.objects.get(staff_id=login_id_)

        except StaffRegister.DoesNotExist:
            print("Invalid staff_id or password")
        else:
            print(password_ == get_staff.password)
            if password_ == get_staff.password:
                request.session['staff_id'] = login_id_
                if request.session['staff_id']:
                    print(request.session.get('staff_id'))
                print("Now, you are logged in")
            else:
                print("Invalid staff_id or password")
    return render(request, 'login.html')

# Create your views here.
