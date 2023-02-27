from django import forms
# from django.contrib.auth.models import User

from core.models import MedicsAppointment, Patient, User

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2',
            }
        ),
    )
    
    last_name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2',
            }
        ),
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control mb-2',
            }
        ),
    )
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",)

        
class PatientProfileForm(forms.ModelForm):
    phone_number = forms.CharField(
        label="Phone Number",
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2',
            }
        ),
        required=True
    )
    
    marital_status = forms.ChoiceField(
        label="Marital Status",
        choices=Patient.MARITAL_STATUS_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control mb-2',
            }
        ),
        required=True
    )
    
    birth_date = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(
            attrs={
                'class': 'form-control mb-2',
            }
        ),
        required=True
    )
    
    blood_group = forms.ChoiceField(
        label="Blood Group",
        choices=Patient.BLOOD_GROUP_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control mb-2',
            }
        ),
        required=True
    )
    
    genotype = forms.ChoiceField(
        choices=Patient.GENOTYPE_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control mb-2',
            }
        ),
        required=True
    )
    class Meta:
        model = Patient
        fields = ("phone_number", "marital_status", "birth_date", "blood_group", "genotype",)
        
class PatientMedicsForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=MedicsAppointment.MEDICS_CATEFORY_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control mb-2',
            }
        ),
        required=True
    )
    case_type = forms.ChoiceField(
        label="Case Type",
        choices=MedicsAppointment.CASE_TYPE_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control mb-2',
            }
        ),
        required=True
    )
    class Meta:
        model = MedicsAppointment
        fields = ("category", "case_type",)
        
        