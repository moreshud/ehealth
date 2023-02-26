from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from core.models import MedicsAppointment, Patient

from core.patient import forms

@login_required(login_url="/sign-in/?next=/patient/")
def dashboard(request):
    user = request.user
    patient = user.patient
    user_form = forms.UserProfileForm(request.POST or None, instance=user)
    patient_form = forms.PatientProfileForm(request.POST or None, instance=patient)
    
    # creating_record = MedicsAppointment.objects.filter(patient=patient).last()
    medics_form = forms.PatientMedicsForm(request.POST or None)
    
    if request.method == "POST":
        request_action = request.POST.get("action")
        
        if request_action == "profile":
            if user_form.is_valid() and patient_form.is_valid():
                patient_form.save()
                user_form.save()
                
        elif request_action == "medics":
            if medics_form.is_valid():
                form_record = medics_form.save(commit=False)
                form_record.patient = patient
                form_record.save()
                
                # MedicsAppointment.objects.create(patient = patient, request.POST)
                
                # form.save()
            # print(request_action)
            # if patient_form.is_valid() and medics_form.is_valid():
            #     continue
            
        return redirect(reverse("patient:dashboard"))
        
    context = {
        "user_form": user_form, 
        "patient_form": patient_form,
        "medics_form": medics_form,
    }
    return render(request, "patient/dashboard.html", context)

# @login_required(login_url="/sign-in/?next=/patient/")
# def medics_appointment(request):
#     user_form = forms.PatientProfileForm()
#     return render(request, "patient/profile.html", {"user_form": user_form})


