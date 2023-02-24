from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "home.html")

def patient_home(request):
    return render(request, "patient-index.html")

def doctor_home(request):
    return render(request, "doctor-index.html")

