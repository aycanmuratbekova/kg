from django.db import models


class ProfessionGroup(models.Model):
    name = models.CharField(max_length=255, verbose_name='Профессия')
    url_name = models.CharField(max_length=255, verbose_name='Профессия латиница', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа Профессии'
        verbose_name_plural = 'Группы Профессий'


class Profession(models.Model):
    profession_group = models.ForeignKey(to=ProfessionGroup, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='professions')
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
    (2, 'ассистент художника-гримера'),
    (3, 'ассистент художника-декоратора'),
    (4, 'ассистент художника-реквизитора'),
)

GENDER = (
    (1, 'Мужчина'),
    (2, 'Женщина'),
)
