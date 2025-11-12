// Интерактивность для ссылок
document.addEventListener('click', function(e) {
    if (e.target.tagName === 'A' && e.target.href.includes('mailto:')) {
        e.preventDefault();
        const email = e.target.textContent;
        if (confirm(`📧 Отправить email на ${email}?`)) {
            window.location.href = e.target.href;
        }
    }
    
    if (e.target.tagName === 'A' && e.target.href.includes('tel:')) {
        e.preventDefault();
        const phone = e.target.textContent;
        if (call(`📱 Позвонить на номер ${phone}?`)) {
            window.location.href = e.target.href;
        }
    }
});