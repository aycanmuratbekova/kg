from django.db import models
from .categories import CATEGORY, VARIOUS_PROPS, SERVICE_CATEGORY


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
    category = models.IntegerField(default=1, choices=SERVICE_CATEGORY, verbose_name="Категория Реквизита")
    name = models.CharField(max_length=255, verbose_name="Название сервиса-услуги")
    url_name = models.CharField(max_length=255, verbose_name="Название сервиса-услуги латиница", unique=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервис-Услуга"
        verbose_name_plural = "Сервисы-Услуги"


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, models.SET_NULL, 'images', null=True, blank=True,
                                verbose_name="фотографии сервиса")
    img = models.ImageField(upload_to='service/%Y/', verbose_name="Фото")
    name = models.CharField(max_length=255, verbose_name="Название картинки", null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class Pavilion(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название павильона")
    url_name = models.CharField(max_length=255, verbose_name="Название павильона латиница", unique=True)
    dimensions = models.CharField(max_length=255, verbose_name='Габариты павильона')
    electrical_connection = models.TextField(verbose_name='Электрподключение')
    options = models.TextField(verbose_name='Опции')
    infrastructure = models.TextField(verbose_name='Инфраструктура')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Павильон"
        verbose_name_plural = "Павильоны"


class PavilionImage(models.Model):
    pavilion = models.ForeignKey(Pavilion, models.CASCADE, 'images', verbose_name="фотографии павильона")
    img = models.ImageField(upload_to='pavilion/%Y/', verbose_name="Фото")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


# Transport и SourceMaterials модельки содержат только один экземпляр

class Transport(models.Model):
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return str(self.id) + "   - Изменить описоние транспорта"

    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорт"


class TransportImage(models.Model):
    transport = models.ForeignKey(Transport, models.CASCADE, 'images', verbose_name="фотографии транспорта")
    img = models.ImageField(upload_to='transport/%Y/', verbose_name="Фото")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class SourceMaterials(models.Model):
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return str(self.id) + "   - Изменить описоние исходных материалов"

    class Meta:
        verbose_name = "Исходные материалы"
        verbose_name_plural = "Исходные материалы"


class SourceMaterialsImage(models.Model):
    transport = models.ForeignKey(SourceMaterials, models.CASCADE, 'images',
                                  verbose_name="фотографии исходных материалов")
    img = models.ImageField(upload_to='source_materials/%Y/', verbose_name="Фото")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
