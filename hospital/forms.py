from django import forms
from django.utils import timezone
from .models import Appointment, Doctor
import datetime

class AppointmentForm(forms.ModelForm):
    # We will use standard fields and do validations in clean()
    appointment_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'min': timezone.localdate().isoformat()
        })
    )
    
    # We will provide default standard slots, which will be updated dynamically by JS
    TIME_SLOTS = [
        ('09:00 AM - 09:30 AM', '09:00 AM - 09:30 AM'),
        ('09:30 AM - 10:00 AM', '09:30 AM - 10:00 AM'),
        ('10:00 AM - 10:30 AM', '10:00 AM - 10:30 AM'),
        ('10:30 AM - 11:00 AM', '10:30 AM - 11:00 AM'),
        ('11:00 AM - 11:30 AM', '11:00 AM - 11:30 AM'),
        ('11:30 AM - 12:00 PM', '11:30 AM - 12:00 PM'),
        ('12:00 PM - 12:30 PM', '12:00 PM - 12:30 PM'),
        ('12:30 PM - 01:00 PM', '12:30 PM - 01:00 PM'),
        ('02:00 PM - 02:30 PM', '02:00 PM - 02:30 PM'),
        ('02:30 PM - 03:00 PM', '02:30 PM - 03:00 PM'),
        ('03:00 PM - 03:30 PM', '03:00 PM - 03:30 PM'),
        ('03:30 PM - 04:00 PM', '03:30 PM - 04:00 PM'),
        ('04:00 PM - 04:30 PM', '04:00 PM - 04:30 PM'),
        ('04:30 PM - 05:00 PM', '04:30 PM - 05:00 PM'),
    ]
    time_slot = forms.ChoiceField(
        choices=TIME_SLOTS,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_time_slot'})
    )

    class Meta:
        model = Appointment
        fields = ['patient_name', 'patient_phone', 'appointment_date', 'time_slot', 'reason']
        widgets = {
            'patient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'patient_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number (e.g. +91 9876543210)'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief description of symptoms/reason for consultation...'}),
        }

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data.get('appointment_date')
        if appointment_date:
            if appointment_date < timezone.localdate():
                raise forms.ValidationError("Appointment date cannot be in the past.")
        return appointment_date

    def clean(self):
        cleaned_data = super().clean()
        doctor = self.instance.doctor if self.instance and hasattr(self.instance, 'doctor') else None
        appointment_date = cleaned_data.get('appointment_date')
        time_slot = cleaned_data.get('time_slot')

        # If doctor wasn't passed in instance initialization, we will handle it in views or check if there's field
        # Usually we pass doctor context in the view, let's handle validation check
        return cleaned_data
