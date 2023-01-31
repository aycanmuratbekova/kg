from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(max_length=255, verbose_name='Фамилия', null=True, blank=True)
    url_name = models.CharField(max_length=255, verbose_name='ФИО латиница')
    profession = models.CharField(max_length=255, verbose_name='Род деятельности')
    bio = models.TextField(verbose_name='Биография')
    photo = models.ImageField(upload_to='person', null=True, blank=False, verbose_name="Фото")

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

    class Meta:
        verbose_name = 'Деятель искусства'
        verbose_name_plural = 'Деятели искусства'
