"""
Проект блог - описание
"""
"""
--------------------------------------
настройка виртуального окружения

python -m venv venv_blog
venv_blog\Scripts\activate

-------------------------------
установка Джанго

python -m pip install Django

-----------------------------------------
создание проекта

django-admin startproject personal_blog .

--------------------------------------------
запуск проекта

python manage.py runserver

--------------------------------------------
создание приложения блог

python manage.py startapp blog
--------------------------------------------
в settings.py - installer app добавляем проект

INSTALLED_APPS = [
    ...
    'blog',
]
----------------------------------------------
models.py - создаём модель для представления БД

---------------------------------------------
миграции

python manage.py makemigrations blog
python manage.py migrate blog

применение основной миграции для проекта

python manage.py migrate
---------------------------------------------
создание админки

python manage.py createsuperuser
admin
admin






















"""