
  // === Telegram Bot Настройки ===
  const BOT_TOKEN = '8581138752:AAEyEJWYZrjo0GjdKowbIk23tA9k7qDr0oY';
  const CHAT_ID = '443467930';
  const TELEGRAM_API = `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`;

  // === Маска телефона ===
  const phoneInput = document.getElementById('phone');
  phoneInput.addEventListener('input', function(e) {
    let value = e.target.value.replace(/\D/g, '');
    if (value.length > 0) {
      value = value.replace(/^(\d)/, '+$1 ');
    }
    if (value.length > 3) {
      value = value.replace(/^(\\+\d+) (\d{3})/, '$1 ($2)');
    }
    if (value.length > 9) {
      value = value.replace(/^(\\+\d+ \(\d{3}\))(\d{3})/, '$1) $2');
    }
    if (value.length > 12) {
      value = value.replace(/^(\\+\d+ \(\d{3}\) \d{3})(\d{2})/, '$1-$2');
    }
    if (value.length > 14) {
      value = value.replace(/^(\\+\d+ \(\d{3}\) \d{3}-\d{2})(\d{2})/, '$1-$2');
    }
    e.target.value = value.slice(0, 18);
  });

  // === Валидация и отправка формы ===
  document.getElementById('requestForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    // Сброс ошибок
    document.querySelectorAll('.error').forEach(el => el.classList.remove('error'));
    document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

    const name = document.getElementById('name').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const dob = document.getElementById('dob').value;
    const genderInput = document.querySelector('input[name="gender"]:checked');
    const message = document.getElementById('message').value.trim();

    const genderMap = { male: 'Мужской', female: 'Женский' };
    const gender = genderInput ? genderMap[genderInput.value] : '';

    let valid = true;

    // Валидация
    if (!name) {
      showError('name', 'Пожалуйста, введите имя.');
      valid = false;
    }

    const phoneRegex = /^[\+]?[0-9\s\-\(\)]{10,18}$/;
    if (!phone) {
      showError('phone', 'Введите номер телефона.');
      valid = false;
    } else if (!phoneRegex.test(phone)) {
      showError('phone', 'Некорректный формат телефона.');
      valid = false;
    }

    if (!dob) {
      showError('dob', 'Выберите дату рождения.');
      valid = false;
    }

    if (!gender) {
      showError('gender', 'Выберите пол.');
      valid = false;
    }

    if (!valid) return;

    // Форматируем сообщение (HTML)
    const birthDate = new Date(dob).toLocaleDateString('ru-RU');

    const text = `
📩 <b>Вам новая заявка:</b>
<b>Имя:</b> ${escapeHtml(name)}
<b>Телефон:</b> ${escapeHtml(phone)}
<b>Дата рождения:</b> ${escapeHtml(birthDate)}
<b>Пол:</b> ${escapeHtml(gender)}
${message ? `<b>Сообщение:</b> ${escapeHtml(message)}` : ''}
    `.trim();

    try {
      const response = await fetch(TELEGRAM_API, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          chat_id: CHAT_ID,
          text: text,
          parse_mode: 'HTML'
        })
      });

      const result = await response.json();

      if (result.ok) {
        // Показать модальное окно
        document.getElementById('successModal').style.display = 'flex';
        // Опционально: сброс формы
        // this.reset();
      } else {
        console.error('Ошибка Telegram API:', result);
        alert('Ошибка отправки: ' + (result.description || 'Неизвестная ошибка'));
      }
    } catch (error) {
      console.error('Ошибка сети:', error);
      alert('Не удалось отправить данные. Проверьте подключение.');
    }
  });

  // Экранирование HTML (защита от багов)
  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Показ ошибки
  function showError(fieldId, message) {
    const input = document.getElementById(fieldId);
    const errorDiv = document.getElementById(fieldId + 'Error');
    input.classList.add('error');
    errorDiv.textContent = message;
  }

  // Закрытие модального окна
  document.getElementById('closeModal').addEventListener('click', () => {
    document.getElementById('successModal').style.display = 'none';
  });

  document.getElementById('successModal').addEventListener('click', function(e) {
    if (e.target === this) {
      this.style.display = 'none';
    }
  });

