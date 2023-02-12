from django.db import models
from .profession import GENDER, ASSISTANT, Profession


class Person(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(max_length=255, verbose_name='Фамилия', null=True, blank=True)
    url_name = models.CharField(max_length=255, verbose_name='ФИО латиница')
    gender = models.PositiveIntegerField(default=1, choices=GENDER, verbose_name='Пол')
    age = models.PositiveIntegerField(verbose_name='Возраст', null=True, blank=True)
    appearance = models.CharField(max_length=255, verbose_name='Внешность', null=True, blank=True)
    # profession = models.CharField(max_length=255, verbose_name='Профессия')
    profession = models.ForeignKey(to=Profession, on_delete=models.SET_NULL, null=True, blank=True, related_name='persons')
    assistant = models.IntegerField(default=1, choices=ASSISTANT,  verbose_name='Ассистент')
    bio = models.TextField(verbose_name='Биография')
    photo = models.ImageField(upload_to='person', null=True, blank=False, verbose_name="Фото")

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

    class Meta:
        verbose_name = 'Деятель искусства'
        verbose_name_plural = 'Деятели искусства'
