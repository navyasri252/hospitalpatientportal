from django.core.management.base import BaseCommand
from hospital.models import Doctor

class Command(BaseCommand):
    help = 'Seeds initial doctor data into the database'

    def handle(self, *args, **kwargs):
        doctors_data = [
            # Cardiology
            {
                'name': 'Sarah Jenkins',
                'department': 'CARDIO',
                'specialization': 'Interventional Cardiology, Heart Failure Specialist',
                'consultation_fee': 150.00,
                'available_days': 'Mon, Wed, Fri',
                'is_active': True
            },
            {
                'name': 'Robert Chen',
                'department': 'CARDIO',
                'specialization': 'Cardiovascular Disease, Echocardiography',
                'consultation_fee': 130.00,
                'available_days': 'Tue, Thu',
                'is_active': True
            },
            # Pediatrics
            {
                'name': 'Emily Rodriguez',
                'department': 'PEDIA',
                'specialization': 'General Pediatrics, Pediatric Allergy',
                'consultation_fee': 95.00,
                'available_days': 'Mon - Thu',
                'is_active': True
            },
            {
                'name': 'William Gupta',
                'department': 'PEDIA',
                'specialization': 'Neonatology, Pediatric Critical Care',
                'consultation_fee': 110.00,
                'available_days': 'Mon, Wed, Fri',
                'is_active': True
            },
            # Orthopedics
            {
                'name': 'David Miller',
                'department': 'ORTHO',
                'specialization': 'Joint Replacement, Sports Medicine',
                'consultation_fee': 140.00,
                'available_days': 'Mon, Tue, Thu',
                'is_active': True
            },
            {
                'name': 'Lisa Park',
                'department': 'ORTHO',
                'specialization': 'Pediatric Orthopedics, Spine Surgery',
                'consultation_fee': 160.00,
                'available_days': 'Wed, Fri',
                'is_active': True
            },
            # Neurology
            {
                'name': 'Marcus Vance',
                'department': 'NEURO',
                'specialization': 'Neurological Disorders, Epilepsy Specialist',
                'consultation_fee': 175.00,
                'available_days': 'Mon - Fri',
                'is_active': True
            },
            {
                'name': 'Aisha Rahman',
                'department': 'NEURO',
                'specialization': 'Stroke Neurologist, Neuroimmunology',
                'consultation_fee': 180.00,
                'available_days': 'Tue, Thu, Fri',
                'is_active': True
            }
        ]

        self.stdout.write(self.style.NOTICE("Seeding Doctors..."))
        for doc in doctors_data:
            doctor, created = Doctor.objects.get_or_create(
                name=doc['name'],
                defaults={
                    'department': doc['department'],
                    'specialization': doc['specialization'],
                    'consultation_fee': doc['consultation_fee'],
                    'available_days': doc['available_days'],
                    'is_active': doc['is_active']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created Doctor: Dr. {doctor.name} ({doctor.get_department_display()})"))
            else:
                self.stdout.write(self.style.WARNING(f"Doctor already exists: Dr. {doctor.name}"))
        
        self.stdout.write(self.style.SUCCESS("Doctor seeding completed successfully!"))
