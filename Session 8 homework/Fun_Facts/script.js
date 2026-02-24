const factData = [
    "I don't have favorite book, music or film; I love them all equally",
    "I love reading books, the genre doesn't matter",
    "I have graduated music school with high ranks but now I am not a good musician at all",
    "I love baking, but not cooking",
    "I am an ambivert"
];

let shuffledFacts = [...factData].sort(() => Math.random() - 0.5);
let count = 0;

const container = document.getElementById('facts-container');
const revealBtn = document.getElementById('reveal-btn');
const resetBtn = document.getElementById('reset-btn');
const counterText = document.getElementById('counter');

revealBtn.addEventListener('click', () => {
    if (count < shuffledFacts.length) {
        const newFact = document.createElement('div');
        newFact.className = 'fact';
        newFact.textContent = shuffledFacts[count];

        // Apply color classes based on count
        if (count < 2) newFact.classList.add('low-count');
        else if (count < 4) newFact.classList.add('mid-count');
        else newFact.classList.add('high-count');

        container.appendChild(newFact);

        // Simple delay to trigger CSS transition
        setTimeout(() => newFact.classList.add('show'), 10);

        count++;
        counterText.textContent = count;
    } else {
        revealBtn.textContent = "All Facts Revealed!";
        revealBtn.style.opacity = "0.5";
    }
});

resetBtn.addEventListener('click', () => {
    container.innerHTML = '';
    count = 0;
    counterText.textContent = "0";
    revealBtn.textContent = "Reveal Secret";
    revealBtn.style.opacity = "1";
    // Reshuffle for a new experience
    shuffledFacts = [...factData].sort(() => Math.random() - 0.5);
});