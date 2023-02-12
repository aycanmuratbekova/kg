from django.db import models


class Profession(models.Model):
    name = models.CharField(max_length=255, verbose_name='Профессия')
    url_name = models.CharField(max_length=255, verbose_name='Профессия латиница', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


PROFESSIONS = (
    (1, 'Режиссёр'),
    (2, 'Сценарист'),
    (3, 'Композитор'),
    (4, 'Художник - постановщик'),
    (5, 'Актёр'),
)
ASSISTANT = (
    (1, 'Не является ассистентом'),
    (2, 'ассистент директорв'),
    (3, 'ассистент сценариста'),
    (4, 'ассистент оператора'),
    (5, 'ассистент художника-гримера'),
    (6, 'ассистент художника-декоратора'),
    (7, 'ассистент художника-реквизитора'),
)

GENDER = (
    (1, 'Мужчина'),
    (2, 'Женщина'),
)
