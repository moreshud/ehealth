from django.contrib import admin
from .models import Doctor, MedicsAppointment, Patient, User

# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MedicsAppointment)
