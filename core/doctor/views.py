from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import MedicsAppointment

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
    
    if request.method == "POST":
        record = MedicsAppointment.objects.get(id=request.POST.get("dataRowId"))
        record.appointment_status = request.POST.get("decision")
        record.save()    
    
    return render(request, "doctor/dashboard.html", {"doctor_records":doctor_records})

