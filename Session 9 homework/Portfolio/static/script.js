/**
 * PORTFOLIO INTERACTIVITY
 * Author: Aylar
 * Features: Dark Mode, Typing Effect, Scroll Reveal, Form Validation, Project Filter
 */

// ===== INITIALIZE ALL FEATURES ON LOAD =====
document.addEventListener('DOMContentLoaded', () => {
    initDarkMode();
    initTypingEffect();
    initScrollReveal();
    initFormValidation();
    initProjectFilter();
    initCounters();
});

// ===== 1. DARK MODE TOGGLE (Saves to localStorage) =====
function initDarkMode() {
    const toggleBtn = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme');

    if (currentTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
    }

    toggleBtn.addEventListener('click', () => {
        let theme = document.documentElement.getAttribute('data-theme');
        if (theme === 'light') {
            document.documentElement.removeAttribute('data-theme');
            localStorage.setItem('theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
        }
    });
}

// ===== 2. TYPING ANIMATION (Hero Section) =====
function initTypingEffect() {
    const textElement = document.getElementById('typing-text');
    const phrases = ["DESIGNER // DEVELOPER", "PROBLEM SOLVER", "CREATIVE CODER"];
    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function type() {
        const currentPhrase = phrases[phraseIndex];
        
        if (isDeleting) {
            textElement.textContent = currentPhrase.substring(0, charIndex - 1);
            charIndex--;
        } else {
            textElement.textContent = currentPhrase.substring(0, charIndex + 1);
            charIndex++;
        }

        let typeSpeed = isDeleting ? 50 : 100;

        if (!isDeleting && charIndex === currentPhrase.length) {
            isDeleting = true;
            typeSpeed = 2000; 
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
        }

        setTimeout(type, typeSpeed);
    }
    type();
}

// ===== 3. SCROLL REVEAL ANIMATIONS =====
function initScrollReveal() {
    const reveals = document.querySelectorAll('.reveal');
    
    const revealOnScroll = () => {
        for (let i = 0; i < reveals.length; i++) {
            const windowHeight = window.innerHeight;
            const elementTop = reveals[i].getBoundingClientRect().top;
            const elementVisible = 150; 

            if (elementTop < windowHeight - elementVisible) {
                reveals[i].classList.add('active');
            }
        }
    };

    // Add the listener to the window
    window.addEventListener('scroll', revealOnScroll);
    // Trigger once on load for elements already in view
    revealOnScroll();
}

// ===== 4. CONTACT FORM VALIDATION =====
function initFormValidation() {
    const form = document.getElementById('contactForm');
    if (!form) return; // Safety check
    
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        let isValid = true;

        const name = document.getElementById('name');
        const email = document.getElementById('email');
        const message = document.getElementById('message');

        if (name.value.trim().length < 2) {
            document.getElementById('nameError').style.display = 'block';
            isValid = false;
        } else {
            document.getElementById('nameError').style.display = 'none';
        }

        if (!email.value.includes('@') || email.value.length < 5) {
            document.getElementById('emailError').style.display = 'block';
            isValid = false;
        } else {
            document.getElementById('emailError').style.display = 'none';
        }

        if (message.value.trim() === '') {
            document.getElementById('messageError').style.display = 'block';
            isValid = false;
        } else {
            document.getElementById('messageError').style.display = 'none';
        }

        if (isValid) {
            form.style.display = 'none';
            document.getElementById('formSuccess').style.display = 'block';
        }
    });
}

// ===== 5. PROJECT FILTER LOGIC =====
function initProjectFilter() {
    const filters = document.querySelectorAll('.filter-btn');
    const projects = document.querySelectorAll('.project-card');

    filters.forEach(btn => {
        btn.addEventListener('click', () => {
            filters.forEach(f => f.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projects.forEach(card => {
                const category = card.getAttribute('data-category');
                
                if (filterValue === 'all' || filterValue === category) {
                    card.classList.remove('hide');
                    card.classList.add('show');
                } else {
                    card.classList.add('hide');
                    card.classList.remove('show');
                }
            });
        });
    });
}


// ===== 6. ANIMATED COUNTERS & PROGRESS BARS =====
function initCounters() {
    const counters = document.querySelectorAll('.counter');
    const bars = document.querySelectorAll('.progress-line span');
    const skillsSection = document.querySelector('#skills');
    
    let animated = false;

    const animateSkills = () => {
        const sectionPos = skillsSection.getBoundingClientRect().top;
        const screenPos = window.innerHeight / 1.3;

        // Start animation when section enters viewport
        if (sectionPos < screenPos && !animated) {
            // Animate Numbers
            counters.forEach(counter => {
                const target = +counter.getAttribute('data-target');
                const updateCount = () => {
                    const current = +counter.innerText;
                    const increment = target / 50; // Speed adjustment

                    if (current < target) {
                        counter.innerText = Math.ceil(current + increment);
                        setTimeout(updateCount, 20);
                    } else {
                        counter.innerText = target;
                    }
                };
                updateCount();
            });

            // Animate Progress Bars
            bars.forEach(bar => {
                bar.style.width = bar.getAttribute('data-width');
            });

            animated = true; // Prevents re-animating
        }
    };

    window.addEventListener('scroll', animateSkills);
}