from django import forms
# from django.contrib.auth.models import User

from core.models import MedicsAppointment, Patient, User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",)

        
class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("phone_number", "marital_status", "birth_date", "blood_group", "genotype",)
        
class PatientMedicsForm(forms.ModelForm):
    class Meta:
        model = MedicsAppointment
        fields = ("category", "case_type",)
        
        