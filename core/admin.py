from django.contrib import admin
from .models import Doctor, MedicsAppointment, Patient, User


admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MedicsAppointment)
