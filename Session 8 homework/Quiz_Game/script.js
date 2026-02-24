// script.js

// 1. Data Structure: Array of 5 questions
const quizData = [
    { q: "Which language runs in a web browser?", a: "JavaScript", options: ["Java", "C", "Python", "JavaScript"] },
    { q: "What does CSS stand for?", a: "Cascading Style Sheets", options: ["Creative Style Sheets", "Cascading Style Sheets", "Computer Style Sheets", "Colorful Style Sheets"] },
    { q: "What year was JavaScript launched?", a: "1995", options: ["1996", "1995", "1994", "None of the above"] },
    { q: "Who created the World Wide Web?", a: "Tim Berners-Lee", options: ["Bill Gates", "Steve Jobs", "Tim Berners-Lee", "Elon Musk"] },
    { q: "What is the result of 2 + '2' in JS?", a: "22", options: ["4", "22", "Error", "NaN"] }
];

let currentQuestionIndex = 0;
let score = 0;
let selectedAnswer = null;

const container = document.getElementById('quiz-container');
const feedbackDiv = document.getElementById('feedback');
const scoreDisplay = document.getElementById('current-score');

// 2. Initialization
function initQuiz() {
    console.log("Quiz initialized..."); // Debug Log 1
    showQuestion();
}

// 3. Render Question
function showQuestion() {
    const currentData = quizData[currentQuestionIndex];
    selectedAnswer = null; // Reset selection
    feedbackDiv.classList.add('hidden');

    container.innerHTML = `
        <p class="question-text">${currentData.q}</p>
        <div id="options-list">
            ${currentData.options.map(opt => `<button class="option-btn">${opt}</button>`).join('')}
        </div>
        <button id="submit-btn">Submit Answer</button>
    `;

    // Add event listeners to new option buttons
    document.querySelectorAll('.option-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            // Remove 'selected' class from others
            document.querySelectorAll('.option-btn').forEach(b => b.classList.remove('selected'));
            e.target.classList.add('selected');
            selectedAnswer = e.target.innerText;
        });
    });

    document.getElementById('submit-btn').addEventListener('click', checkAnswer);
}

// 4. Logic to check answer
function checkAnswer() {
    // Error Handling: Check if an option was selected
    if (!selectedAnswer) {
        alert("Please select an answer before submitting!");
        console.warn("User attempted to submit without selection."); // Debug Log 2
        return;
    }

    const correctAnswer = quizData[currentQuestionIndex].a;
    feedbackDiv.classList.remove('hidden');

    if (selectedAnswer === correctAnswer) {
        score++;
        feedbackDiv.innerText = "Correct! Well done.";
        feedbackDiv.className = "feedback correct";
    } else {
        feedbackDiv.innerText = `Incorrect. The right answer was: ${correctAnswer}`;
        feedbackDiv.className = "feedback incorrect";
    }

    scoreDisplay.innerText = score;
    
    // Replace Submit button with Next button
    const submitBtn = document.getElementById('submit-btn');
    submitBtn.id = "next-btn";
    submitBtn.innerText = "Next Question";
    submitBtn.removeEventListener('click', checkAnswer);
    submitBtn.addEventListener('click', nextQuestion);
}

// 5. Navigation Logic
function nextQuestion() {
    currentQuestionIndex++;
    
    if (currentQuestionIndex < quizData.length) {
        showQuestion();
    } else {
        showFinalScore();
    }
}

function showFinalScore() {
    console.log(`Quiz finished. Final Score: ${score}/5`); // Debug Log 3
    container.innerHTML = `
        <h2>Quiz Complete!</h2>
        <p>You scored ${score} out of ${quizData.length}</p>
        <button onclick="location.reload()">Restart Quiz</button>
    `;
    feedbackDiv.classList.add('hidden');
}

initQuiz();