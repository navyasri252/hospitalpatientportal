from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.utils import timezone
from .models import Doctor, Appointment, MedicalReport, Patient
from .forms import AppointmentForm

def home(request):
    doctors_count = Doctor.objects.filter(is_active=True).count()
    appointments_count = Appointment.objects.count()
    pending_count = Appointment.objects.filter(status='PENDING').count()
    
    context = {
        'doctors_count': doctors_count,
        'appointments_count': appointments_count,
        'pending_count': pending_count,
        'departments': Doctor.DEPARTMENTS,
    }
    return render(request, 'hospital/home.html', context)

def doctor_list(request):
    department_filter = request.GET.get('dept', '')
    doctors = Doctor.objects.filter(is_active=True)
    
    if department_filter:
        doctors = doctors.filter(department=department_filter)
        
    context = {
        'doctors': doctors,
        'departments': Doctor.DEPARTMENTS,
        'selected_dept': department_filter,
    }
    return render(request, 'hospital/doctor_list.html', context)

def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id, is_active=True)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            
            # Double-booking check
            date = form.cleaned_data['appointment_date']
            slot = form.cleaned_data['time_slot']
            
            if Appointment.objects.filter(doctor=doctor, appointment_date=date, time_slot=slot).exists():
                form.add_error('time_slot', 'This time slot is already booked for this doctor. Please choose another.')
            else:
                try:
                    appointment.save()
                    
                    # Also create or check Patient profile by phone
                    patient_phone = form.cleaned_data['patient_phone']
                    patient_name = form.cleaned_data['patient_name']
                    Patient.objects.get_or_create(
                        phone=patient_phone,
                        defaults={'name': patient_name}
                    )
                    
                    messages.success(request, f"Appointment with Dr. {doctor.name} booked successfully!")
                    return redirect('appointment_success', appointment_id=appointment.id)
                except IntegrityError:
                    form.add_error('time_slot', 'A double-booking error occurred. Please select another slot.')
    else:
        # Default value for form
        initial_date = request.GET.get('date', timezone.localdate().isoformat())
        form = AppointmentForm(initial={'appointment_date': initial_date})
        
    context = {
        'doctor': doctor,
        'form': form,
    }
    return render(request, 'hospital/book_appointment.html', context)

def appointment_success(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'hospital/appointment_success.html', {'appointment': appointment})

def patient_dashboard(request):
    phone = request.GET.get('phone', '').strip()
    appointments = []
    searched = False
    
    if phone:
        appointments = Appointment.objects.filter(patient_phone=phone).order_by('-appointment_date', '-created_at')
        searched = True
        
    # Group appointments into active and history
    upcoming = []
    past = []
    
    for app in appointments:
        if app.appointment_date >= timezone.localdate() and app.status in ['PENDING', 'CONFIRMED']:
            upcoming.append(app)
        else:
            past.append(app)
            
    context = {
        'upcoming': upcoming,
        'past': past,
        'phone': phone,
        'searched': searched,
    }
    return render(request, 'hospital/patient_dashboard.html', context)

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Access denied. Only staff users are allowed.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'hospital/admin_login.html', {'form': form})

def admin_logout(request):
    logout(request)
    return redirect('home')

@staff_member_required(login_url='admin_login')
def admin_dashboard(request):
    status_filter = request.GET.get('status', '')
    appointments = Appointment.objects.all().order_by('-appointment_date', '-created_at')
    
    if status_filter:
        appointments = appointments.filter(status=status_filter)
        
    stats = {
        'total': Appointment.objects.count(),
        'pending': Appointment.objects.filter(status='PENDING').count(),
        'confirmed': Appointment.objects.filter(status='CONFIRMED').count(),
        'completed': Appointment.objects.filter(status='COMPLETED').count(),
        'cancelled': Appointment.objects.filter(status='CANCELLED').count(),
    }
    
    context = {
        'appointments': appointments,
        'selected_status': status_filter,
        'stats': stats,
        'status_choices': Appointment.STATUS_CHOICES,
    }
    return render(request, 'hospital/admin_dashboard.html', context)

@staff_member_required(login_url='admin_login')
def update_appointment_status(request, appointment_id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=appointment_id)
        new_status = request.POST.get('status')
        if new_status in dict(Appointment.STATUS_CHOICES):
            appointment.status = new_status
            appointment.save()
            messages.success(request, f"Appointment for {appointment.patient_name} updated to {appointment.get_status_display()}.")
    return redirect('admin_dashboard')

@staff_member_required(login_url='admin_login')
def add_medical_report(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    # We only write report if status is COMPLETED
    if request.method == 'POST':
        diagnosis = request.POST.get('diagnosis')
        prescription = request.POST.get('prescription')
        notes = request.POST.get('notes', '')
        
        report, created = MedicalReport.objects.update_or_create(
            appointment=appointment,
            defaults={
                'diagnosis': diagnosis,
                'prescription': prescription,
                'notes': notes
            }
        )
        
        # Mark as completed automatically if not already
        if appointment.status != 'COMPLETED':
            appointment.status = 'COMPLETED'
            appointment.save()
            
        messages.success(request, f"Medical report for {appointment.patient_name} saved successfully.")
        return redirect('admin_dashboard')
        
    return redirect('admin_dashboard')

def get_booked_slots(request):
    doctor_id = request.GET.get('doctor_id')
    date_str = request.GET.get('date')
    
    if not doctor_id or not date_str:
        return JsonResponse({'error': 'Missing parameters'}, status=400)
        
    try:
        booked_slots = list(Appointment.objects.filter(
            doctor_id=doctor_id,
            appointment_date=date_str
        ).exclude(status='CANCELLED').values_list('time_slot', flat=True))
        return JsonResponse({'booked_slots': booked_slots})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
