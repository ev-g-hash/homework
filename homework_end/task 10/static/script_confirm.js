// Дополнительное подтверждение удаления
document.addEventListener('DOMContentLoaded', function() {
    const deleteBtn = document.getElementById('deleteBtn');
    let clicked = false;
    
    deleteBtn.addEventListener('click', function(e) {
        if (!clicked) {
            e.preventDefault();
            clicked = true;
            
            this.innerHTML = '⚠️ Нажмите еще раз для подтверждения';
            this.style.background = 'linear-gradient(45deg, #d32f2f, #b71c1c)';
            
            setTimeout(() => {
                this.innerHTML = '🗑️ Да, удалить навсегда';
                this.style.background = '';
                clicked = false;
            }, 3000);
        } else {
            this.innerHTML = '⏳ Удаляем...';
            this.disabled = true;
        }
    });
    
    // Предупреждение при загрузке страницы
    setTimeout(() => {
        alert('⚠️ ВНИМАНИЕ! Вы собираетесь удалить пользователя {{ user.name }}.\n\nЭто действие нельзя отменить. Пожалуйста, будьте уверены в своем решении.');
    }, 1000);
});