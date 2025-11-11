from django.db import models


class User(models.Model):
    """
    Модель пользователя для хранения профиля.
    """
    name = models.CharField("Имя", max_length=100, blank=False, null=False)
    age = models.PositiveIntegerField("Возраст", null=True, blank=True)
    phone = models.CharField("Телефон", max_length=20, blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['id']

    def __str__(self):
        return f"{self.name} (ID: {self.id})"
