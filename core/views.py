from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from . import forms
from .models import Doctor, Patient, User
# Create your views here.

def home(request):
    return render(request, "home.html")


def sign_up(request):
    form = forms.SignUpForm()
    
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get("email").lower()
            user = form.save(commit=False)
            user.email = email
            user.save()
            
            login(request, user)
            
            if form.cleaned_data.get("user_type") == User.USER_TYPE_CHOICES[0][0]: #DOCTOR
                Doctor.objects.create(doctor=user)
                return redirect("/doctor/")
            
            Patient.objects.create(patient=user)
            return redirect("/patient/") 
            
    return render(request, "sign-up.html", {
        "form": form
    })

@login_required()
def patient_home(request):
    return render(request, "patient-index.html")

@login_required()
def doctor_home(request):
    return render(request, "doctor-index.html")

