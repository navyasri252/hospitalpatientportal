# HealthHub Screenshots

This folder contains screenshots of the HealthHub Hospital Management System user interface.

## Screenshots to Add

To generate and add screenshots to this folder, follow these steps:

1. Start the Django development server:
   ```bash
   python manage.py runserver 127.0.0.1:8000
   ```

2. Take screenshots of each page and save them as PNG files:

   - **home.png**: Homepage
     - URL: http://127.0.0.1:8000/
     - Shows the landing page with "Healthcare Made Simple & Accessible" banner and department cards

   - **doctor-list.png**: Doctor Listing Page
     - URL: http://127.0.0.1:8000/doctors/
     - Shows all doctors with their specialties, consultation fees, and availability

   - **book-appointment.png**: Appointment Booking Form
     - URL: http://127.0.0.1:8000/book/1/
     - Shows the booking form with patient details, date selection, and time slot picker

   - **patient-login.png**: Patient Login Page
     - URL: http://127.0.0.1:8000/patient-login/
     - Shows phone-based authentication form for patients

   - **admin-login.png**: Admin/Staff Login Page
     - URL: http://127.0.0.1:8000/admin-panel/login/
     - Shows staff portal authentication interface

3. Save each screenshot as a PNG file in this directory with the corresponding filename.

4. Commit and push the screenshots to GitHub:
   ```bash
   git add .
   git commit -m "Add UI screenshots"
   git push origin main
   ```

## Screenshot Specifications

- **Resolution**: 1200x800px or higher for better visibility
- **Format**: PNG files (lossless compression)
- **Quality**: Full page screenshots showing the complete interface
- **Theme**: Light theme (current HealthHub design)

## Tools for Taking Screenshots

You can use any of these tools:
- Built-in Windows Snipping Tool
- Print Screen (then paste in an image editor)
- VS Code integrated browser screenshot feature
- Third-party tools like ShareX, Greenshot, or Lightshot
