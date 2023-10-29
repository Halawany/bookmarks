// Navbar
function openNav() {
  document.getElementById("mySidenav").style.width = "100%";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

// Bookmarks box
// document.querySelector('.box').addEventListener('click', function () {
//   // Example: Alert a message when the box is clicked
//   alert('Box clicked! You can perform actions here.');
// });

// Edit popup
const editButton = document.querySelector('.option.edit');
const editPopup = document.querySelector('.popup#editPopup');
const editClose = document.querySelector('.close#editClose');
const saveEditButton = document.getElementById('saveEdit');
const cancelEditButton = document.getElementById('cancelEdit');

// Initially hide the popup
editPopup.style.display = 'none';

editButton.addEventListener('click', () => {
  editPopup.style.display = 'block';
});

editClose.addEventListener('click', () => {
  editPopup.style.display = 'none';
});

saveEditButton.addEventListener('click', () => {
  // Handle saving the edit data here
  editPopup.style.display = 'none';
});

cancelEditButton.addEventListener('click', () => {
  // Handle canceling the edit action here
  editPopup.style.display = 'none';
});

// Delete popup
const deleteButton = document.querySelector('.option.delete');
const deletePopup = document.querySelector('.popup#deletePopup');
const deleteClose = document.querySelector('.close#deleteClose');
const confirmDeleteButton = document.getElementById('confirmDelete');
const cancelDeleteButton = document.getElementById('cancelDelete');

// Initially hide the delete popup
deletePopup.style.display = 'none';

deleteButton.addEventListener('click', () => {
  deletePopup.style.display = 'block';
});

deleteClose.addEventListener('click', () => {
  deletePopup.style.display = 'none';
});

confirmDeleteButton.addEventListener('click', () => {
  // Handle the delete action here
  deletePopup.style.display = 'none';
});

cancelDeleteButton.addEventListener('click', () => {
  deletePopup.style.display = 'none';
});