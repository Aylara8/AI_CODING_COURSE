const essayInput = document.getElementById('essay-input');
const goalInput = document.getElementById('word-goal');
const currentCountDisplay = document.getElementById('current-count');
const statusMsg = document.getElementById('status-msg');

function updateCounter() {
    // 1. Get the text and clean it
    const text = essayInput.value.trim();
    
    // 2. Split by spaces/newlines and filter out empty strings
    // Logic: text.split(/\s+/) uses "Regex" to find any whitespace
    const words = text === "" ? [] : text.split(/\s+/);
    const wordCount = words.length;
    
    // 3. Get the goal
    const goal = parseInt(goalInput.value) || 0;
    
    // 4. Update the display
    currentCountDisplay.innerText = wordCount;

    // 5. Calculate difference
    const diff = goal - wordCount;

    if (diff > 0) {
        statusMsg.innerText = `Meýilnamadan ${diff} söz yzda`;
        statusMsg.className = "value under";
    } else if (diff === 0) {
        statusMsg.innerText = "Meýilnama doly ýerine ýetirildi!";
        statusMsg.className = "value met";
    } else {
        statusMsg.innerText = `Meýilnamadan ${Math.abs(diff)} söz artykmaç`;
        statusMsg.className = "value met";
    }
}

// Listen for typing in the textarea
essayInput.addEventListener('input', updateCounter);

// Listen for changes in the goal input
goalInput.addEventListener('input', updateCounter);