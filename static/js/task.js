function confirmDelete() {
    const isConfirmed = confirm("Are you sure you want to delete this task?");
    if (isConfirmed) {
        document.getElementById("delete-form").submit(); 
    }
}
