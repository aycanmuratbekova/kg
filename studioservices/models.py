from django.db import models
from .categories import CATEGORY, VARIOUS_PROPS


class Props(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название реквизита")
    url_name = models.CharField(max_length=255, verbose_name="Название реквизита латиница", unique=True)
    category = models.IntegerField(default=1, choices=CATEGORY, verbose_name="Категория Реквизита")
    various_props = models.IntegerField(default=1, choices=VARIOUS_PROPS, verbose_name="Вид Разнообразного Реквизита")
    img = models.ImageField(upload_to='props/%Y/', verbose_name="Фото")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Костюм и реквизит"
        verbose_name_plural = "Костюмы и реквизиты"


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название сервиса-услуги")
    url_name = models.CharField(max_length=255, verbose_name="Название сервиса-услуги латиница", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервис-Услуга"
        verbose_name_plural = "Сервисы-Услуги"


class ServiceCategory(models.Model):
    service = models.ForeignKey(Service, models.SET_NULL, 'service_categories', null=True, blank=True,
                                verbose_name="Сервис-Услуга")
    name = models.CharField(max_length=255, verbose_name="Название подкатегории сервиса")
    url_name = models.CharField(max_length=255, verbose_name="Название подкатегории сервиса латиница", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория сервиса"
        verbose_name_plural = "Подкаатегории сервиса"


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, models.SET_NULL, 'images', null=True, blank=True,
                                verbose_name="фотографии сервиса")
    img = models.ImageField(upload_to='props/%Y/', verbose_name="Фото")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"