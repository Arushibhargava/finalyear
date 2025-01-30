// Go back to the previous page
function goBack() {
    history.back();
}

// Form submission handling
document.getElementById("projectForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const projectName = document.getElementById("projectName").value;
    const description = document.getElementById("description").value;
    const techStack = document.getElementById("techStack").value;

    if (projectName && description && techStack) {
        alert(`Project Submitted!\n\nName: ${projectName}\nDescription: ${description}\nTech Stack: ${techStack}`);
        
        // Redirect to the dashboard page after submission
        window.location.href = "tdashboard.html";
    } else {
        alert("Please fill out all fields.");
    }
});


