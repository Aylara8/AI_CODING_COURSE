// --- GLOBAL STATE ---
let timerInterval;
let secondsElapsed = 0;
let isRunning = false;

document.addEventListener('DOMContentLoaded', () => {
    // Initial data load
    loadItems();

    // Requirement: Live Search (Interactive Feature)
    const searchInput = document.getElementById('live-search');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();
            const rows = document.querySelectorAll('.session-row');
            rows.forEach(row => {
                const subject = row.querySelector('.subject-tag').textContent.toLowerCase();
                row.style.display = subject.includes(term) ? '' : 'none';
            });
        });
    }
});

// --- CORE DATA FUNCTIONS ---

// Requirement: Fetch API (AJAX)
async function loadItems() {
    toggleLoading(true);
    try {
        const response = await fetch('/api/items');
        const data = await response.json();
        renderAll(data.items);
    } catch (error) {
        console.error("Failed to load items:", error);
    } finally {
        toggleLoading(false);
    }
}

function renderAll(items) {
    const list = document.getElementById('session-list');
    const totalTimeEl = document.getElementById('total-time');
    const countEl = document.getElementById('sessions-count');
    
    if (!list) return;

    list.innerHTML = '';
    let totalMinutes = 0;
    
    // Sort items by date (newest first)
    items.sort((a, b) => new Date(b.date) - new Date(a.date));

    items.forEach(item => {
        totalMinutes += parseInt(item.duration);
        
        const row = document.createElement('tr');
        row.className = 'session-row';
        row.id = `session-${item.id}`; // Crucial for deletion
        row.setAttribute('data-date', item.date);
        
        row.innerHTML = `
            <td>${item.date}</td>
            <td class="subject-tag"><strong>${item.subject}</strong></td>
            <td>${item.duration} mins</td>
            <td>
                <button onclick="confirmDelete(${item.id})" class="btn-delete" title="Delete Session">🗑️</button>
            </td>
        `;
        list.appendChild(row);
    });

    // Update Stats Display
    if (totalTimeEl) totalTimeEl.innerText = totalMinutes;
    if (countEl) countEl.innerText = items.length;
}

// --- INTERACTIVE FEATURES ---

// Requirement: Filter by Date Range
function filterByDate() {
    const start = document.getElementById('filter-start').value;
    const end = document.getElementById('filter-end').value;
    const rows = document.querySelectorAll('.session-row');

    rows.forEach(row => {
        const rowDate = row.getAttribute('data-date');
        let visible = true;

        if (start && rowDate < start) visible = false;
        if (end && rowDate > end) visible = false;

        row.style.display = visible ? '' : 'none';
    });
}

// Requirement: Confirm Delete (AJAX)
function confirmDelete(id) {
    if (confirm('Are you sure you want to remove this session?')) {
        deleteItem(id);
    }
}

async function deleteItem(id) {
    try {
        const response = await fetch(`/api/delete/${id}`, { method: 'DELETE' });
        const result = await response.json();
        
        if (result.success) {
            // Remove from UI immediately for "Smooth transition"
            const row = document.getElementById(`session-${id}`);
            if (row) row.remove();
            
            // Re-fetch to update the total time/stats correctly
            loadItems(); 
        }
    } catch (error) {
        alert("Error deleting item.");
    }
}

// --- TIMER FEATURE ---
function toggleTimer() {
    const btn = document.getElementById('start-stop-btn');
    const display = document.getElementById('timer-display');
    const durationInput = document.getElementById('duration');

    if (!isRunning) {
        isRunning = true;
        btn.innerText = "Stop & Fill";
        btn.classList.add('timer-running');
        timerInterval = setInterval(() => {
            secondsElapsed++;
            let mins = Math.floor(secondsElapsed / 60);
            let secs = secondsElapsed % 60;
            display.innerText = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
        }, 1000);
    } else {
        isRunning = false;
        clearInterval(timerInterval);
        btn.innerText = "Start Timer";
        btn.classList.remove('timer-running');
        
        // Fill the duration field (convert seconds to minutes, minimum 1)
        if (durationInput) {
            durationInput.value = Math.max(1, Math.round(secondsElapsed / 60));
        }
        secondsElapsed = 0;
    }
}

// UI Helper
function toggleLoading(show) {
    const spinner = document.getElementById('loading-spinner');
    if (spinner) spinner.className = show ? '' : 'hidden';
}