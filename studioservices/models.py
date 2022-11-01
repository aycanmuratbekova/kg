from django.db import models


class PropsCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория реквизитов"
        verbose_name_plural = "Категории реквизитов"


class Props(models.Model):
    category = models.ForeignKey(PropsCategory, models.SET_NULL, 'props', null=True, blank=True, verbose_name="категория реквизита")
    name = models.CharField(max_length=255, verbose_name="Название реквизита")
    img = models.ImageField(upload_to='props/%Y/', verbose_name="Фото")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Реквизит"
        verbose_name_plural = "Реквизиты"