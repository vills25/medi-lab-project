from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import CounterTable,Features, doctor, ReportType, Patient

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(CounterTable)
admin.site.register(Features)
admin.site.register(doctor)
admin.site.register(ReportType)
admin.site.register(Patient)

# Register your models here.
