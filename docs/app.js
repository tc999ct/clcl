// Todo Web App with task completion tracking
document.addEventListener('DOMContentLoaded', () => {
    const taskInput = document.getElementById('taskInput');
    const addButton = document.getElementById('addButton');
    const taskList = document.getElementById('taskList');

    // Load tasks from localStorage
    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    // Render tasks
    function renderTasks() {
        taskList.innerHTML = '';
        tasks.forEach((task, index) => {
            const li = document.createElement('li');
            li.textContent = task.text;
            li.dataset.index = index;

            // Apply strikethrough if task is done
            if (task.done) {
                li.style.textDecoration = 'line-through';
                li.style.color = '#888';
            }

            // Toggle completion on click
            li.style.cursor = 'pointer';
            li.addEventListener('click', () => {
                toggleTaskDone(index);
            });

            // Create delete button
            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Delete';
            deleteBtn.className = 'delete-btn';
            deleteBtn.dataset.index = index;
            deleteBtn.addEventListener('click', (e) => {
                e.stopPropagation(); // Prevent triggering li click
                deleteTask(index);
            });

            li.appendChild(deleteBtn);
            taskList.appendChild(li);
        });
    }

    // Add new task
    function addTask() {
        const text = taskInput.value.trim();
        if (text) {
            tasks.push({ text: text, done: false });
            localStorage.setItem('tasks', JSON.stringify(tasks));
            taskInput.value = '';
            renderTasks();
        }
    }

    // Toggle task completion
    function toggleTaskDone(index) {
        tasks[index].done = !tasks[index].done;
        localStorage.setItem('tasks', JSON.stringify(tasks));
        renderTasks();
    }

    // Delete task
    function deleteTask(index) {
        tasks.splice(index, 1);
        localStorage.setItem('tasks', JSON.stringify(tasks));
        renderTasks();
    }

    // Event Listeners
    addButton.addEventListener('click', addTask);
    taskInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            addTask();
        }
    });

    // Initial render
    renderTasks();
});