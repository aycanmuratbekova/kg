from django.db import models


class PropsCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")

    def __str__(self):
        return self.name


class Props(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название реквизита")
    img = models.ImageField(upload_to='props/%Y/', verbose_name="Фото")

    def __str__(self):
        return self.name
