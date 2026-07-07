// Interactive Time Slot Picker JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const dateInput = document.getElementById('id_appointment_date');
    const formTimeSlotSelect = document.getElementById('id_time_slot');
    const slotGrid = document.getElementById('slot-picker-grid');
    const submitBtn = document.getElementById('submit-booking-btn');

    // List of time slots matching choice values in form
    const timeSlotsList = [
        '09:00 AM - 09:30 AM',
        '09:30 AM - 10:00 AM',
        '10:00 AM - 10:30 AM',
        '10:30 AM - 11:00 AM',
        '11:00 AM - 11:30 AM',
        '11:30 AM - 12:00 PM',
        '12:00 PM - 12:30 PM',
        '12:30 PM - 01:00 PM',
        '02:00 PM - 02:30 PM',
        '02:30 PM - 03:00 PM',
        '03:00 PM - 03:30 PM',
        '03:30 PM - 04:00 PM',
        '04:00 PM - 04:30 PM',
        '04:30 PM - 05:00 PM'
    ];

    let selectedSlot = '';

    // Initialize or load slots for the default date
    if (dateInput && dateInput.value) {
        fetchAndRenderSlots(dateInput.value);
    }

    // Change date event
    if (dateInput) {
        dateInput.addEventListener('change', function() {
            selectedSlot = '';
            formTimeSlotSelect.value = '';
            submitBtn.disabled = true;
            fetchAndRenderSlots(this.value);
        });
    }

    function fetchAndRenderSlots(dateStr) {
        if (!dateStr || !doctorId) return;

        slotGrid.innerHTML = '<div class="text-center w-100 py-3"><div class="spinner-border spinner-border-sm text-primary" role="status"></div><span class="ms-2">Checking slot availability...</span></div>';

        const apiEndpoint = `/api/booked-slots/?doctor_id=${doctorId}&date=${dateStr}`;

        fetch(apiEndpoint)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response error');
                }
                return response.json();
            })
            .then(data => {
                const bookedSlots = data.booked_slots || [];
                renderSlots(bookedSlots);
            })
            .catch(error => {
                console.error('Error fetching booked slots:', error);
                slotGrid.innerHTML = '<div class="alert alert-danger w-100 mb-0">Failed to load slot availability. Please try refreshing or choosing another date.</div>';
            });
    }

    function renderSlots(bookedSlots) {
        slotGrid.innerHTML = '';
        
        timeSlotsList.forEach(slot => {
            const isBooked = bookedSlots.includes(slot);
            
            const btn = document.createElement('div');
            btn.className = 'slot-btn';
            btn.textContent = slot;
            
            if (isBooked) {
                btn.classList.add('booked');
                btn.title = 'This slot is already booked';
            } else {
                // Attach click handler for selection
                btn.addEventListener('click', function() {
                    // Deselect previous selection
                    const currentSelected = slotGrid.querySelector('.slot-btn.selected');
                    if (currentSelected) {
                        currentSelected.classList.remove('selected');
                    }
                    
                    // Select this slot
                    btn.classList.add('selected');
                    selectedSlot = slot;
                    
                    // Set form hidden select element
                    formTimeSlotSelect.value = slot;
                    
                    // Enable submit button
                    submitBtn.disabled = false;
                });
            }
            
            slotGrid.appendChild(btn);
        });
    }
});
