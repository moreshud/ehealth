from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.

STATUS = [
    ("ACTIVE", "ACTIVE"),
    ("INACTIVE", "INACTIVE"),
]

class TimestampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
        
class User(AbstractUser, TimestampedModel):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    
    USER_TYPE_CHOICES = [
        ("DOCTOR", "DOCTOR"),
        ("PATIENT", "PATIENT"),
    ]
    username = None
    email = models.EmailField(_('email address'), unique=True)
    
    objects = UserManager()
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="", null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="PATIENT")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Patient(TimestampedModel):
    MARITAL_STATUS_CHOICES = [
        ('SINGLE', 'SINGLE'),
        ('MARRIED', 'MARRIED'),
        ('DIVORCED', 'DIVORCED'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    GENOTYPE_CHOICES = [
        ('AA', 'AA'),
        ('AB', 'AB'),
        ('AS', 'AS'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # avatar = 
    phone_number = models.CharField(max_length=200, unique=True, null=True, blank=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES, null=True, blank=True)
    genotype = models.CharField(max_length=10, choices=GENOTYPE_CHOICES, blank=True)
    status = models.CharField(max_length=8, choices=STATUS, default="ACTIVE")
    
    def __str__(self) -> str:
        return self.user.email
    
class Doctor(TimestampedModel):
    SPECIALITY_CHOICES = [
        ("GENERAL", "GENERAL"),
        ("SURGEON", "SURGEON"),
        ("PEDIATRIC", "PEDIATRIC"),
        ("PHYSIATRIST", 'PHYSIATRIST'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,)
    speciality = models.CharField(max_length=20, choices=SPECIALITY_CHOICES, default="GENERAL")
    status = models.CharField(max_length=8, choices=STATUS, default="ACTIVE")
    
    def __str__(self) -> str:
        return self.user.email


class MedicsAppointment(TimestampedModel):
    MEDICS_CATEFORY_CHOICES = [
        ("MALARIA", "MALARIA"),
        ("TYPHOID", "TYPHOID"),
        ("SURGERY", "SURGERY"),
        ("MENTAL HEALTH", "MENTAL HEALTH"),
        ("OTHER", "OTHER"),
    ]
    
    APPOINTEMENT_SESSION_CHOICES = [
        ("MORNING", "MORNING"),
        ("AFTERNOON", "AFTERNOON"),
        ("EVENING", "EVENING"),
    ]
    
    CASE_TYPE_CHOICES = [
        ("CHECKUP", "CHECKUP"),
        ("REPORT", "REPORT"),
        ("EMERGENCY", "EMERGENCY"),
    ]
    
    APPOINTMENT_STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("CONFIRMED", "CONFIRMED"),
        ("CANCELLED", "CANCELLED"),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # doctor
    category = models.CharField(max_length=20, choices=MEDICS_CATEFORY_CHOICES, default="MALARIA")
    case_type = models.CharField(max_length=10, choices=CASE_TYPE_CHOICES, default=CASE_TYPE_CHOICES[0][0])
    appointment_booked = models.BooleanField(default=False)
    session = models.CharField(max_length=20, choices=APPOINTEMENT_SESSION_CHOICES, default=APPOINTEMENT_SESSION_CHOICES[0][0])
    
    # appointment_date
    appointment_staus = models.CharField(max_length=10, choices=APPOINTMENT_STATUS_CHOICES, default=APPOINTMENT_STATUS_CHOICES[0][0])
    
    def __str__(self) -> str:
        return self.patient.user.email