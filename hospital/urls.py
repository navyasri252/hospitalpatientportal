from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('appointment/success/<int:appointment_id>/', views.appointment_success, name='appointment_success'),
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/update/<int:appointment_id>/', views.update_appointment_status, name='update_appointment_status'),
    path('admin-panel/report/<int:appointment_id>/', views.add_medical_report, name='add_medical_report'),
    path('api/booked-slots/', views.get_booked_slots, name='get_booked_slots'),
    
    # Custom simple login/logout for admin-panel without full auth machinery
    path('admin-panel/login/', views.admin_login, name='admin_login'),
    path('admin-panel/logout/', views.admin_logout, name='admin_logout'),
]
