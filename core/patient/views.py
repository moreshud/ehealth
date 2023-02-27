from collections import Counter
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count
from core.models import MedicsAppointment, Patient

from core.patient import forms

@login_required(login_url="/sign-in/?next=/patient/")
def dashboard(request):
    user = request.user
    patient = user.patient
    user_form = forms.UserProfileForm(request.POST or None, instance=user)
    patient_form = forms.PatientProfileForm(request.POST or None, instance=patient)
    medics_form = forms.PatientMedicsForm(request.POST or None)
    appointment_form = forms.PatientAppointmentForm(request.POST or None)
    
    
    def categorical_data_counts(filterer, field):
        return filterer.values(field).annotate(count=Count(field)).order_by('-count',)
    
    patient_records_filter = MedicsAppointment.objects.filter(patient=patient).order_by('-created_on')
    records = patient_records_filter.order_by('-created_on', 'appointment_date')
    category_counts = categorical_data_counts(patient_records_filter, "category")[:3]
    case_type_counts = categorical_data_counts(patient_records_filter, "case_type")[:3]
        
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
        elif request_action == "appointment":
            if appointment_form.is_valid():
                appointment = appointment_form.save(commit=False)
                appointment.appointment_booked = True
                appointment.patient = patient
                # appointment.doctor = selected_doctor
                appointment.save()
            pass
            
        return redirect(reverse("patient:dashboard"))
        
    context = {
        "user_form": user_form, 
        "patient_form": patient_form,
        "medics_form": medics_form,
        "appointment_form": appointment_form,
        "records": records,
        "category_counts": category_counts,
        "case_type_counts": case_type_counts,
    }
    
    # forms:{user: user_form}
    # data :{records: records}
    return render(request, "patient/dashboard.html", context)


