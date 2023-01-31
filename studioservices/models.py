from django.db import models


class PropsCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория услуг и реквизитов"
        verbose_name_plural = "Категории услуг и реквизитов"


class Props(models.Model):
    category = models.ForeignKey(PropsCategory, models.SET_NULL, 'props', null=True, blank=True, verbose_name="категория реквизита")
    name = models.CharField(max_length=255, verbose_name="Название реквизита")
    img = models.ImageField(upload_to='props/%Y/', verbose_name="Фото")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Реквизит"
        verbose_name_plural = "Реквизиты"


class Service(models.Model):
    category = models.ForeignKey(PropsCategory, models.SET_NULL, 'services', null=True, blank=True, verbose_name="категория услуг")
    name = models.CharField(max_length=255, verbose_name="Название услуги")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, models.SET_NULL, 'images', null=True, blank=True,
                                verbose_name="фотографии услуги")
    img = models.ImageField(upload_to='props/%Y/', verbose_name="Фото")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"