from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class TimestampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
# class User(AbstractUser, TimestampedModel):
#     GENDER_CHOICES = [
#         ("Male", "Male"),
#         ("Female", "Female"),
#     ]
    
#     USER_TYPE_CHOICES = [
#         ("DOCTOR", "DOCTOR"),
#         ("PATIENT", "PATIENT"),
#     ]

#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="", null=True)
#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="PATIENT")


# class Patient(TimestampedModel):
#     MARITAL_STATUS_CHOICES = [
#         ('SINGLE', 'SINGLE'),
#         ('MARRIED', 'MARRIED'),
#         ('DIVORCED', 'DIVORCED'),
#     ]
    
#     BLOOD_GROUP_CHOICES = [
#         ('A+', 'A+'),
#         ('A-', 'A-'),
#         ('B+', 'B+'),
#         ('B-', 'B-'),
#         ('AB+', 'AB+'),
#         ('AB-', 'AB-'),
#         ('O+', 'O+'),
#         ('O-', 'O-'),
#     ]
    
#     GENOTYPE_CHOICES = [
#         ('AA', 'AA'),
#         ('AB', 'AB'),
#         ('AS', 'AS'),
#     ]
#     patient = models.OneToOneField("User", on_delete=models.CASCADE)
#     # avatar = 
#     phone_number = models.CharField(max_length=200, unique=True, null=True, blank=True)
#     martial_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True)
#     # brith_date
#     blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES, blank=True)
#     genotype = models.CharField(max_length=10, choices=GENOTYPE_CHOICES, blank=True)
#     # status
    
#     # def __str__(self):
#     #     return self.patient.user.full_name
    
    


# class Doctor(TimestampedModel):
#     SPECIALITY_CHOICES = [
#         (1, "GENERAL"),
#         (2, "SURGEON"),
#         (3, "PEDIATRIC"),
#         (4, 'PHYSIATRIST'),
#     ]
    
#     # avatar 
#     speciality = models.PositiveSmallIntegerField(choices=SPECIALITY_CHOICES, default=1)
    # status

# class MedicalRecord(TimestampedModel):
#     MEDICS_CATEFORY_CHOICES = [
#         (1, "CHECKUP"),
#         (2, "MALARIA FEVER"),
#         (3, "TYPHOID"),
#         (4, "SURGERY"),
#         (5, 'MENTAL ISSUES'),
#         (6, 'OTHRE'),
#     ]
#     # patient
#     # doctor
#     category = models.PositiveSmallIntegerField(choices=MEDICS_CATEFORY_CHOICES, default=1)
    
    
# class Appointment(TimestampedModel):
#     APPOINTEMENT_SESSION_CHOICES = [
#         (1, "MORNING"),
#         (2, "AFTERNOON"),
#         (3, "EVENING"),
#     ]
    
#     CASE_TYPE_CHOICES = [
#         (1, "CHECKUP"),
#         (2, "REPORT"),
#         (3, "EMERGENCY"),
#     ]
    
#     APPOINTMENT_STATUS_CHOICES = [
#         ("PENDING", "PENDING"),
#         ("CONFIRMED", "CONFIRMED"),
#         ("CANCELLED", "CANCELLED"),
#     ]
#     # medical_rec
#     session = models.PositiveSmallIntegerField(choices=APPOINTEMENT_SESSION_CHOICES, default=1)
#     case_type = models.PositiveSmallIntegerField(choices=CASE_TYPE_CHOICES, default=1)
#     # appointment_date
#     appointment_staus = models.CharField(max_length=10, choices=APPOINTMENT_STATUS_CHOICES, default="PENDING")