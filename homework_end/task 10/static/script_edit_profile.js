// // Интерактивность для формы редактирования
// document.addEventListener('DOMContentLoaded', function() {
//     const form = document.getElementById('editForm');
//     const saveBtn = document.getElementById('saveBtn');
    
//     // Отслеживание изменений в форме
//     let hasChanges = false;
//     const inputs = form.querySelectorAll('input');
    
//     inputs.forEach(input => {
//         input.addEventListener('change', function() {
//             hasChanges = true;
//             saveBtn.style.background = 'linear-gradient(45deg, #ff9800, #f57c00)';
//             saveBtn.innerHTML = '⚠️ Сохранить изменения';
//         });
//     });
    
//     form.addEventListener('submit', function(e) {
//         if (!hasChanges) {
//             if (!confirm('ℹ️ Вы не внесли никаких изменений. Продолжить?')) {
//                 e.preventDefault();
//                 return;
//             }
//         }
        
//         saveBtn.innerHTML = '⏳ Сохраняем...';
//         saveBtn.disabled = true;
        
//         setTimeout(() => {
//             saveBtn.innerHTML = '✅ Сохранено!';
//             setTimeout(() => {
//                 saveBtn.innerHTML = '💾 Сохранить изменения';
//                 saveBtn.disabled = false;
//                 hasChanges = false;
//             }, 1000);
//         }, 1500);
//     });
    
//     // Предупреждение при уходе со страницы с несохраненными изменениями
//     window.addEventListener('beforeunload', function(e) {
//         if (hasChanges) {
//             e.preventDefault();
//             e.returnValue = '⚠️ У вас есть несохраненные изменения. Вы уверены, что хотите уйти?';
//         }
//     });
// });
