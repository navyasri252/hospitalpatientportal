// JavaScript powered Instant Doctor Filtering by department

document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const doctorCards = document.querySelectorAll('.doctor-card-item');

    // Parse URL search parameters in case we came from Home page links
    const urlParams = new URLSearchParams(window.location.search);
    const deptParam = urlParams.get('dept');
    
    if (deptParam) {
        // Set the active button matching the URL parameter
        filterButtons.forEach(btn => {
            if (btn.getAttribute('data-filter') === deptParam) {
                setActiveButton(btn);
            }
        });
        filterDoctors(deptParam);
    }

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filterValue = this.getAttribute('data-filter');
            
            // Highlight active button
            setActiveButton(this);
            
            // Filter doctors card list
            filterDoctors(filterValue);
        });
    });

    function setActiveButton(activeButton) {
        filterButtons.forEach(btn => btn.classList.remove('active'));
        activeButton.classList.add('active');
    }

    function filterDoctors(filterValue) {
        doctorCards.forEach(card => {
            const cardDept = card.getAttribute('data-department');
            
            if (filterValue === 'all' || cardDept === filterValue) {
                // Show card with a brief transition animation
                card.style.display = 'block';
                setTimeout(() => {
                    card.style.opacity = '1';
                    card.style.transform = 'scale(1)';
                }, 50);
            } else {
                // Hide card
                card.style.opacity = '0';
                card.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    card.style.display = 'none';
                }, 300); // matches transition time
            }
        });
    }
});
