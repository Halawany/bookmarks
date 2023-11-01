// Get all the sidebar links
const sidebarLinks = document.querySelectorAll('.sidebar-link');

// Add a click event listener to each link
sidebarLinks.forEach(link => {
    link.addEventListener('click', function() {
        // Remove the "active" class from all links
        sidebarLinks.forEach(link => {
            link.classList.remove('active');
        });

        // Add the "active" class to the clicked link
        this.classList.add('active');
    });
});

