document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;

    // --- DELETE RESOURCE AJAX ---
    document.addEventListener('click', async (e) => {
        const btn = e.target.closest('.delete-res-btn');
        if (!btn) return;

        const resourceId = btn.getAttribute('data-id');
        const column = document.getElementById(`resource-col-${resourceId}`);
        const icon = btn.querySelector('i');

        if (!confirm('Are you sure you want to delete this resource?')) return;

        btn.disabled = true;
        const originalIconClass = icon.className;
        icon.className = 'spinner-border spinner-border-sm';

        // Log the ID to ensure JS is picking it up from the HTML correctly
        console.log("Attempting to delete ID:", resourceId);

        try {
            // Using a relative path to ensure it hits your Flask server correctly
            const response = await fetch('/api/delete/' + resourceId, {
                method: 'POST',
                headers: { 
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }
            });

            console.log("Response Status:", response.status);

            if (response.status === 404) {
                throw new Error("Server says this route does not exist (404). Check app.py!");
            }

            const data = await response.json();

            if (data.success) {
                column.style.transition = 'all 0.4s ease';
                column.style.opacity = '0';
                column.style.transform = 'scale(0.9)';
                
                setTimeout(() => {
                    column.remove();
                    if (document.querySelectorAll('.resource-card').length === 0) {
                        location.reload();
                    }
                }, 400);
            } else {
                alert('Error: ' + (data.error || 'Delete failed'));
                resetBtn();
            }
        } catch (err) {
            console.error("Full Error Info:", err);
            alert('Status: ' + err.message);
            resetBtn();
        }

        function resetBtn() {
            btn.disabled = false;
            icon.className = originalIconClass;
        }
    });

    // --- THEME TOGGLE ---
    const applyTheme = (theme) => {
        htmlElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        if(toggleBtn) toggleBtn.innerHTML = theme === 'light' ? '<span>🌙</span>' : '<span>☀️</span>';
    };
    const savedTheme = localStorage.getItem('theme') || 'light';
    applyTheme(savedTheme);
    if(toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            const newTheme = htmlElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
            applyTheme(newTheme);
        });
    }
});

