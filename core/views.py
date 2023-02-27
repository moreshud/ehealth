from django.shortcuts import render, redirect
from django.contrib.auth import login

from . import forms
from .models import Doctor, Patient, User
# Create your views here.

def home(request):
    return render(request, "home.html")


def sign_up(request):
    form = forms.SignUpForm()
    
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        user_type = request.POST.get("user_type")
        
        if form.is_valid():
            email = form.cleaned_data.get("email").lower()
            user = form.save(commit=False)
            # user.email = email
            user.user_type = user_type
            user.save()
            
            login(request, user)
            
            if  user_type == User.USER_TYPE_CHOICES[0][0]: #DOCTOR
                Doctor.objects.create(user=user)
                return redirect("/doctor/")
            
            Patient.objects.create(user=user)
            return redirect("/patient/") 
            
    return render(request, "sign-up.html", {
        "form": form
    })

