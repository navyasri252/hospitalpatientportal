from django.contrib import admin
from .models import Doctor, Patient, Appointment, MedicalReport

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'specialization', 'consultation_fee', 'available_days', 'is_active')
    list_filter = ('department', 'is_active')
    search_fields = ('name', 'specialization')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date_of_birth', 'created_at')
    search_fields = ('name', 'phone', 'email')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'patient_phone', 'doctor', 'appointment_date', 'time_slot', 'status')
    list_filter = ('status', 'appointment_date', 'doctor')
    search_fields = ('patient_name', 'patient_phone')

@admin.register(MedicalReport)
class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'diagnosis', 'created_at')
    search_fields = ('appointment__patient_name', 'diagnosis')
