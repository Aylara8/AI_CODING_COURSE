// Select the button we just created
const themeBtn = document.getElementById('theme-btn');

themeBtn.addEventListener('click', function() {
    // 1. Change the Page Title dynamically
    document.title = "Üýtgedilen Sahypa!";

    // 2. Change the Meta Description
    let metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) {
        metaDesc.content = "Reňkler we süzgüçler üýtgedildi.";
    }

    // 3. Change the Body Background and Text Color
    // This provides a visual confirmation that the JS is working
    document.body.style.backgroundColor = "#006400"; // Deep Green
    document.body.style.color = "white";

    // 4. Inject a specific style to the Head to hide all horizontal rules
    const style = document.createElement('style');
    style.textContent = "hr { border: 1px solid yellow; }";
    document.head.appendChild(style);

    alert("Web sahypanyň 'Head' bölümi we reňkleri üýtgedildi!");
});