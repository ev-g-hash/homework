// Интерактивность формы созданияdocument.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('createForm');
    const submitBtn = document.getElementById('submitBtn');
    
    form.addEventListener('submit', function(e) {
        submitBtn.innerHTML = '⏳ Создаем пользователя...';
        submitBtn.disabled = true;
        
        // Анимация загрузки
        setTimeout(() => {
            submitBtn.innerHTML = '✅ Готово!';
            setTimeout(() => {
                submitBtn.innerHTML = '✅ Создать пользователя';
                submitBtn.disabled = false;
            }, 1000);
        }, 1500);
    });
    
    // Валидация в реальном времени
    const inputs = form.querySelectorAll('input');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value.trim()) {
                this.style.borderColor = '#4CAF50';
                this.style.boxShadow = '0 0 10px rgba(76, 175, 80, 0.3)';
            } else {
                this.style.borderColor = '#f44336';
                this.style.boxShadow = '0 0 10px rgba(244, 67, 54, 0.3)';
            }
        });
        
        input.addEventListener('focus', function() {
            this.style.borderColor = '#667eea';
            this.style.boxShadow = '0 0 20px rgba(102, 126, 234, 0.3)';
        });
    });
});