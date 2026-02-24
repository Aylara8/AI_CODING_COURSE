const dictionary = {
    "teh": "the",
    "dont": "don't",
    "i": "I",
    "recieve": "receive",
    "adress": "address",
    "seperate": "separate",
    "grammar": "grammar",
    "neccessary": "necessary"
};

const essayInput = document.getElementById('essay-input');
const suggestionContainer = document.getElementById('suggestion-container');
const suggestionList = document.getElementById('suggestion-list');
const checkBtn = document.getElementById('check-btn');

function runFullCheck() {
    console.log("Checking essay..."); // This helps us debug
    const text = essayInput.value;
    
    // 1. Word Count & Status
    const words = text.trim() === "" ? [] : text.trim().split(/\s+/);
    const wordCount = words.length;
    document.getElementById('current-count').innerText = wordCount;

    const goal = parseInt(document.getElementById('word-goal').value) || 0;
    const statusMsg = document.getElementById('status-msg');
    const diff = goal - wordCount;
    statusMsg.innerText = diff > 0 ? `${diff} words remaining` : `${Math.abs(diff)} words over goal`;

    // 2. Grammar/Spell Check
    suggestionList.innerHTML = ""; 
    let errorsFound = 0;
    const seen = new Set();

    const cleanWords = text.toLowerCase().replace(/[.,!?;:]/g, " ").split(/\s+/);

    cleanWords.forEach(word => {
        if (dictionary[word] && !seen.has(word)) {
            errorsFound++;
            seen.add(word);
            
            const btn = document.createElement('button');
            btn.className = "suggestion-item";
            btn.style.display = "block"; // Ensure it's visible
            btn.style.margin = "5px 0";
            btn.innerHTML = `Change <b>"${word}"</b> to <b>"${dictionary[word]}"</b>`;
            
            btn.onclick = function() {
                const regex = new RegExp(`\\b${word}\\b`, 'gi');
                essayInput.value = essayInput.value.replace(regex, dictionary[word]);
                runFullCheck(); 
            };
            suggestionList.appendChild(btn);
        }
    });

    suggestionContainer.style.display = errorsFound > 0 ? "block" : "none";
}

// Event Listeners
essayInput.addEventListener('input', runFullCheck);
checkBtn.addEventListener('click', runFullCheck);