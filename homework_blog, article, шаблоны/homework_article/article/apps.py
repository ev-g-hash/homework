from django.apps import AppConfig


class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'article'
    verbose_name = 'Разные модели (Article - Статьи), (Group - Группы), (Category - Категории), (Person-Клиенты)'
