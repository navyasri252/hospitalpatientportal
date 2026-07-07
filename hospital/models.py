from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    DEPARTMENTS = [
        ('CARDIO', 'Cardiology'),
        ('PEDIA', 'Pediatrics'),
        ('ORTHO', 'Orthopedics'),
        ('NEURO', 'Neurology'),
    ]
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=10, choices=DEPARTMENTS)
    specialization = models.CharField(max_length=150)
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    available_days = models.CharField(max_length=100, default="Mon - Fri")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.name} ({self.get_department_display()})"

class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Confirmation'),
        ('CONFIRMED', 'Confirmed'),
        ('COMPLETED', 'Consultation Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    patient_name = models.CharField(max_length=100)
    patient_phone = models.CharField(max_length=15)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    time_slot = models.CharField(max_length=20, help_text="e.g. 10:00 AM - 10:30 AM")
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['doctor', 'appointment_date', 'time_slot']

    def __str__(self):
        return f"{self.patient_name} with Dr. {self.doctor.name} on {self.appointment_date}"

class MedicalReport(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='medical_report')
    diagnosis = models.TextField()
    prescription = models.TextField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.appointment.patient_name} - {self.appointment.appointment_date}"
