async function deleteBook(bookId) {
    if (!confirm("Are you sure you want to remove this book?")) return;

    // Show loading state
    const element = document.getElementById(`book-${bookId}`);
    element.style.opacity = '0.5';

    try {
        const response = await fetch(`/delete/${bookId}`, { method: 'DELETE' });
        if (response.ok) {
            element.remove();
        } else {
            alert("Failed to delete.");
            element.style.opacity = '1';
        }
    } catch (err) {
        console.error("Error:", err);
    }
}