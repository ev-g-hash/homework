// Интерактивность для кнопок
        document.addEventListener('click', function(e) {
            if (e.target.classList.contains('btn')) {
                e.target.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    e.target.style.transform = '';
                }, 150);
            }
        });
        
        // Анимация для форм
        document.addEventListener('focus', function(e) {
            if (e.target.tagName === 'INPUT') {
                e.target.parentElement.style.transform = 'scale(1.02)';
                setTimeout(() => {
                    e.target.parentElement.style.transform = '';
                }, 200);
            }
        }, true);
        
        // Подтверждение для критических действий
        document.addEventListener('submit', function(e) {
            if (e.target.action.includes('delete_user')) {
                if (!confirm('⚠️ Вы уверены, что хотите удалить этого пользователя? Это действие нельзя отменить!')) {
                    e.preventDefault();
                }
            }
        });
        
        // Эффект печатающей машинки для заголовков
        function typeWriter(element, text, speed = 100) {
            let i = 0;
            element.innerHTML = '';
            function type() {
                if (i < text.length) {
                    element.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(type, speed);
                }
            }
            type();
        }
        
        // Применяем эффект к заголовкам
        document.addEventListener('DOMContentLoaded', function() {
            const headers = document.querySelectorAll('h1, h2');
            headers.forEach(header => {
                const originalText = header.textContent;
                if (originalText.trim()) {
                    setTimeout(() => {
                        typeWriter(header, originalText, 50);
                    }, 1000);
                }
            });
        });