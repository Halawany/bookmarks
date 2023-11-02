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

// Delete Bookmark
document.getElementById("deleteButton").addEventListener("click", function() {
    // Add your code for deleting the bookmark here
    alert("Bookmark deleted!");
});

document.getElementById("cancelButton").addEventListener("click", function() {
    // Add your code for canceling the delete operation here
    alert("Deletion canceled!");
});