from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import MedicsAppointment
from django.db.models import Count


from core.patient import forms
# Create your views here.

@login_required()
def dashboard(request):
    user = request.user
    doctor = user.doctor
    # medics_form = forms.PatientMedicsForm(request.POST or None)
    doctor_records = MedicsAppointment.objects.filter(doctor=doctor).order_by(
        "-created_on", "-appointment_status",
    )
    
    def categorical_data_counts(filterer, field):
        return (
            filterer.values(field)
            .annotate(count=Count(field))
            .order_by(
                "-count",
            )
        )
    appointment_status_counts = categorical_data_counts(doctor_records, "appointment_status")
    diagnosis_counts = categorical_data_counts(doctor_records, "category")[:3]
    sensitivity_counts =categorical_data_counts(doctor_records, "case_type")[:3]
    
    
    if request.method == "POST":
        record = MedicsAppointment.objects.get(id=request.POST.get("dataRowId"))
        record.appointment_status = request.POST.get("decision")
        record.save()    
    
    context = {
        "doctor_records":doctor_records,
        "appointment_status_counts": appointment_status_counts,
        "diagnosis_counts": diagnosis_counts,
        "sensitivity_counts": sensitivity_counts
    }
    return render(request, "doctor/dashboard.html", context)

