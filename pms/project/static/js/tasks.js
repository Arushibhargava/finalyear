// Sidebar navigation highlighting
const menuItems = document.querySelectorAll('.sidebar nav ul li');
menuItems.forEach((item) => {
    item.addEventListener('click', () => {
        menuItems.forEach((menu) => menu.classList.remove('active'));
        item.classList.add('active');
    });
});

// Add Task button functionality
document.querySelector('.add-task-btn').addEventListener('click', () => {
    alert('Add Task functionality can be implemented here!');
});

// Logout functionality
document.querySelector('.logout-btn').addEventListener('click', () => {
    alert('You have logged out!');
});

// Navigation Function
function navigateTo(page) {
    window.location.href = page;
}

// Open Add Task Form Modal
function openAddTaskForm() {
    document.getElementById('add-task-modal').style.display = 'flex';
}

// Close Add Task Form Modal
function closeAddTaskForm() {
    document.getElementById('add-task-modal').style.display = 'none';
}

// Add Task Functionality
function addTask(event) {
    event.preventDefault();

    const title = document.getElementById('document-title').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;

    // Add new task to table
    const table = document.getElementById('tasks-list');
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${title}</td>
        <td>${startDate}</td>
        <td>${endDate}</td>
        <td><button class="upload-btn">Upload</button></td>
        <td>
            <select>
                <option value="pending">Pending</option>
                <option value="updated">Updated</option>
            </select>
        </td>
    `;
    table.appendChild(row);

    // Reset form and close modal
    document.getElementById('add-task-form').reset();
    closeAddTaskForm();
}
// Navigation Function
function navigateTo(page) {
    window.location.href = page;
}

// Open Add Task Form Modal
function openAddTaskForm() {
    document.getElementById('add-task-modal').style.display = 'flex';
}

// Close Add Task Form Modal
function closeAddTaskForm() {
    document.getElementById('add-task-modal').style.display = 'none';
}

// Add Task Functionality
function addTask(event) {
    event.preventDefault();

    const title = document.getElementById('document-title').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;

    // Add new task to table
    const table = document.getElementById('tasks-list');
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${title}</td>
        <td>${startDate}</td>
        <td>${endDate}</td>
        <td>
            <label class="upload-label">Upload</label>
            <input type="file" class="file-input" onchange="handleFileUpload(this)">
        </td>
        <td>
            <select>
                <option value="pending">Pending</option>
                <option value="updated">Updated</option>
            </select>
        </td>
    `;
    table.appendChild(row);

    // Reset form and close modal
    document.getElementById('add-task-form').reset();
    closeAddTaskForm();
}

// Handle File Upload
function handleFileUpload(input) {
    if (input.files.length > 0) {
        const fileName = input.files[0].name;
        alert(`File "${fileName}" uploaded successfully!`);
    }
}
