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
    
    def categorical_data_counts(filter, field):
        return filter.values(field).annotate(count=Count(field)).order_by('-count')
    records = MedicsAppointment.objects.filter(patient=patient).order_by('-created_on')
    # category_counts = records.values('category',).annotate(count=Count('category')).order_by('-count',)
    category_counts = categorical_data_counts(records, "category")[:3]
    case_type_counts = categorical_data_counts(records, "case_type")
    
    
    # category_case_type_sum_values = Counter()
    # for row in category_counts:
    #     category_case_type_sum_values[row['category']] += row['count']
    #     category_case_type_sum_values[row['case_type']] += row['count']
        
    # print(category_case_type_sum_values)
        
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
            
        return redirect(reverse("patient:dashboard"))
        
    context = {
        "user_form": user_form, 
        "patient_form": patient_form,
        "medics_form": medics_form,
        "records": records,
        "category_counts": category_counts,
        "case_type_counts": case_type_counts,
    }
    return render(request, "patient/dashboard.html", context)

# @login_required(login_url="/sign-in/?next=/patient/")
# def medics_appointment(request):
#     user_form = forms.PatientProfileForm()
#     return render(request, "patient/profile.html", {"user_form": user_form})


