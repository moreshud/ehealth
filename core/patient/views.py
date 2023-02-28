from collections import Counter
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count
from core.models import Doctor, MedicsAppointment, Patient

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
    
    distinct_doctors = Doctor.objects.all().order_by("-user")
    patient_records_filter = MedicsAppointment.objects.filter(patient=patient).order_by('-created_on', '-updated_on')
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
                medic_record = MedicsAppointment.objects.get(id = request.POST.get('dataRowId'))
                medic_record.appointment_date = request.POST.get('appointment_date')      
                medic_record.appointment_booked = True
                medic_record.doctor = Doctor.objects.get(user = request.POST.get("doctor"))    
                medic_record.save()
                            
        return redirect(reverse("patient:dashboard"))
        
    context = {
        "user_form": user_form, 
        "patient_form": patient_form,
        "medics_form": medics_form,
        "appointment_form": appointment_form,
        "distinct_doctors": distinct_doctors,
        "records": records,
        "category_counts": category_counts,
        "case_type_counts": case_type_counts,
    }
    
    # forms:{user: user_form}
    # data :{records: records}
    return render(request, "patient/dashboard.html", context)


