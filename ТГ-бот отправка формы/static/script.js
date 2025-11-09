// === Кастомный мультиселект ===
    const multiselect = document.getElementById('hobbyMultiselect');
    const dropdown = multiselect.querySelector('.multiselect-dropdown');
    const selectedTags = document.getElementById('selectedHobbies');
    const placeholder = document.getElementById('hobbyPlaceholder');
    const checkboxes = dropdown.querySelectorAll('input[type="checkbox"]');

    let selectedHobbies = [];

    multiselect.addEventListener('click', (e) => {
      e.stopPropagation();
      multiselect.classList.toggle('active');
    });

    checkboxes.forEach(checkbox => {
      checkbox.addEventListener('change', () => {
        const value = checkbox.value;
        if (checkbox.checked) {
          if (!selectedHobbies.includes(value)) {
            selectedHobbies.push(value);
          }
        } else {
          selectedHobbies = selectedHobbies.filter(h => h !== value);
        }
        updateSelectedTags();
      });
    });

    function updateSelectedTags() {
      selectedTags.innerHTML = '';
      if (selectedHobbies.length === 0) {
        placeholder.textContent = 'Выберите хобби';
        return;
      }
      placeholder.textContent = `${selectedHobbies.length} выбрано`;
      selectedHobbies.forEach(hobby => {
        const tag = document.createElement('div');
        tag.className = 'selected-tag';
        tag.textContent = hobbyLabel(hobby);
        selectedTags.appendChild(tag);
      });
    }

    function hobbyLabel(value) {
      const labels = {
        reading: 'Чтение',
        sports: 'Спорт',
        music: 'Музыка',
        travel: 'Путешествия'
      };
      return labels[value] || value;
    }

    document.addEventListener('click', () => {
      multiselect.classList.remove('active');
    });

    // === Telegram Bot API ===
    const BOT_TOKEN = '8581138752:AAEyEJWYZrjo0GjdKowbIk23tA9k7qDr0oY';
    const CHAT_ID = '443467930';
    const TELEGRAM_API = `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`;

    // === Форма и валидация ===
    const form = document.getElementById('surveyForm');
    form.addEventListener('submit', async function (e) {
      e.preventDefault();

      // Сброс ошибок
      document.querySelectorAll('.error').forEach(el => el.classList.remove('error'));
      document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

      let valid = true;

      const firstName = document.getElementById('firstName').value.trim();
      const lastName = document.getElementById('lastName').value.trim();
      const dob = document.getElementById('dob').value;
      const genderInput = document.querySelector('input[name="gender"]:checked');
      const notes = document.getElementById('notes').value.trim();

      const genderMap = { male: 'Мужской', female: 'Женский' };
      const gender = genderInput ? genderMap[genderInput.value] : '';

      // Валидация
      if (!firstName) {
        showError('firstName', 'Пожалуйста, введите имя.');
        valid = false;
      }
      if (!lastName) {
        showError('lastName', 'Пожалуйста, введите фамилию.');
        valid = false;
      }
      if (!dob) {
        showError('dob', 'Пожалуйста, выберите дату рождения.');
        valid = false;
      }
      if (!gender) {
        showError('gender', 'Пожалуйста, выберите пол.');
        valid = false;
      }
      if (selectedHobbies.length === 0) {
        showError('hobbies', 'Выберите хотя бы одно хобби.');
        valid = false;
      }

      if (!valid) return;

      // Форматируем сообщение (HTML)
      const formatHobbies = selectedHobbies.map(h => hobbyLabel(h)).join(', ');
      const birthDate = new Date(dob).toLocaleDateString('ru-RU');

      const message = `
📩 <b>Вам новая заявка:</b>
<b>Имя:</b> ${escapeHtml(firstName)}
<b>Фамилия:</b> ${escapeHtml(lastName)}
<b>Дата рождения:</b> ${birthDate}
<b>Пол:</b> ${escapeHtml(gender)}
<b>Хобби:</b> ${escapeHtml(formatHobbies)}
${notes ? `<b>Примечание:</b> ${escapeHtml(notes)}` : ''}
      `.trim();

      try {
        const response = await fetch(TELEGRAM_API, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            chat_id: CHAT_ID,
            text: message,
            parse_mode: 'HTML'
          })
        });

        const result = await response.json();

        if (result.ok) {
          document.getElementById('successModal').style.display = 'flex';
          form.reset();
          selectedHobbies = [];
          updateSelectedTags();
        } else {
          console.error('Telegram API error:', result);
          alert('Ошибка отправки: ' + (result.description || 'Неизвестная ошибка'));
        }
      } catch (error) {
        console.error('Network error:', error);
        alert('Не удалось отправить данные. Проверьте подключение.');
      }
    });

    // Экранирование HTML
    function escapeHtml(text) {
      const div = document.createElement('div');
      div.textContent = text;
      return div.innerHTML;
    }

    function showError(fieldName, message) {
      const input = document.getElementById(fieldName);
      const errorDiv = document.getElementById(fieldName + 'Error');
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