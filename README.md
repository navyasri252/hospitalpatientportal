# HealthHub - Hospital Patient Appointment Management Portal

A modern, responsive web application for managing hospital appointments, patient profiles, and medical reports. Built with Django and Bootstrap 5 with a glassmorphism design.

## Features

### For Patients
- **Easy Appointment Booking**: Book appointments with doctors from various specialties
- **Multiple Departments**: Cardiology, Pediatrics, Orthopedics, Neurology
- **Time Slot Selection**: Interactive slot picker with real-time availability checking
- **Patient Portal**: View upcoming and past appointments
- **Medical Reports**: Access consultation reports and prescriptions
- **Session-based Authentication**: Automatic login after first appointment booking
- **Responsive Design**: Works seamlessly on desktop and mobile devices

### For Admin/Staff
- **Admin Dashboard**: Comprehensive appointment management interface
- **Appointment Status Tracking**: PENDING, CONFIRMED, COMPLETED, CANCELLED
- **Medical Report Management**: Add, edit, and manage consultation reports
- **Doctor Management**: Manage doctor profiles, specializations, and availability
- **Appointment Filtering**: Filter by status, date, and patient information
- **Statistics Dashboard**: Real-time appointment and booking statistics

## Tech Stack

- **Backend**: Django 6.0.6
- **Database**: SQLite
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **JavaScript**: Interactive slot selection, dynamic filtering
- **Server**: Gunicorn (Production), Django Dev Server (Development)
- **Hosting Ready**: Configured for Render deployment

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/navyasri252/hospitalpatientportal.git
   cd hospitalpatientportal
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Admin Superuser**
   ```bash
   python manage.py createsuperuser
   # Or run the script:
   python create_superuser.py
   ```

6. **Collect Static Files** (for production)
   ```bash
   python manage.py collectstatic --no-input
   ```

## Running the Application

### Development Server
```bash
python manage.py runserver 127.0.0.1:8000
```

Visit `http://127.0.0.1:8000/` in your browser.

### Admin Panel Access
- URL: `http://127.0.0.1:8000/admin-panel/login/`
- Default credentials: `admin` / `admin123`

### Staff Django Admin
- URL: `http://127.0.0.1:8000/admin/`
- Use Django superuser credentials

## Usage

### As a Patient
1. Navigate to the home page
2. Click "Book Appointment Now"
3. Select a doctor and specialty
4. Choose appointment date and time slot
5. Enter your name and phone number
6. Confirm booking
7. You'll be auto-logged in and can access your patient portal

### As Admin Staff
1. Login to admin panel with staff credentials
2. View all appointments on the dashboard
3. Update appointment status (Confirmed, Completed, Cancelled)
4. Add medical reports with diagnosis and prescriptions
5. Track appointment statistics and patient data

## Project Structure

```
Hospital-Management/
├── hospital/                    # Main Django app
│   ├── migrations/              # Database migrations
│   ├── management/              # Custom management commands
│   │   └── commands/
│   │       └── seed_doctors.py  # Doctor data seeding script
│   ├── templates/               # HTML templates
│   │   └── hospital/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── doctor_list.html
│   │       ├── book_appointment.html
│   │       ├── patient_login.html
│   │       ├── patient_dashboard.html
│   │       ├── admin_login.html
│   │       └── admin_dashboard.html
│   ├── models.py                # Database models
│   ├── views.py                 # View logic
│   ├── forms.py                 # Django forms
│   ├── urls.py                  # URL routing
│   └── admin.py                 # Admin configuration
├── myproject/                   # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/                      # Static files
│   ├── css/
│   │   └── style.css            # Custom styling
│   └── js/
│       ├── doctor_filter.js     # Department filtering
│       └── slot_selector.js     # Time slot selection
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── render.yaml                  # Render deployment config
└── README.md
```

## Database Models

### Doctor
- Name, Department, Specialization
- Consultation Fee
- Available Days
- Active/Inactive Status

### Patient
- Name, Phone (unique), Email
- Date of Birth
- Creation timestamp

### Appointment
- Patient Name & Phone
- Doctor (Foreign Key)
- Appointment Date & Time Slot
- Reason for Visit
- Status (PENDING, CONFIRMED, COMPLETED, CANCELLED)
- Timestamps

### MedicalReport
- Appointment (OneToOne)
- Diagnosis
- Prescription
- Doctor Notes
- Creation timestamp

## Features Implemented

✅ Patient appointment booking system
✅ Automatic patient profile creation on first booking
✅ Session-based patient authentication
✅ Admin appointment management dashboard
✅ Medical report creation and viewing
✅ Real-time slot availability checking
✅ Department-based doctor filtering
✅ Responsive glassmorphic UI
✅ Multiple appointment status tracking
✅ Patient appointment history
✅ Consultation report viewing

## Color Scheme

- **Primary**: Blue-Teal gradient
- **Background**: Light blue-purple gradient
- **Accents**: Pink, Purple, Cyan
- **Text**: Dark slate

## Dependencies

Key Python packages:
- Django 6.0.6
- Gunicorn
- WhiteNoise (Static file serving)
- python-decouple (Environment variables)

See `requirements.txt` for complete list.

## Deployment

### Render Deployment
The project includes `render.yaml` for easy deployment to Render:

```yaml
buildCommand: pip install -r requirements.txt && python manage.py collectstatic --no-input
startCommand: gunicorn myproject.wsgi:application
```

### Environment Variables
- `PYTHON_VERSION`: 3.11.0
- `WEB_CONCURRENCY`: 2 (Memory optimized)

## Future Enhancements

- Email notifications for appointments
- SMS reminders
- Doctor availability calendar
- Patient medical history
- Prescription management
- Payment integration
- Video consultation support
- Rating and review system

## Contributing

Contributions are welcome! Please feel free to submit pull requests or issues.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the GitHub repository:
https://github.com/navyasri252/hospitalpatientportal/issues

## Author

Developed as a comprehensive hospital management solution for appointment scheduling and patient care management.