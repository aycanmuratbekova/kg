from django.db import models
from PIL import Image


class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    url_name = models.CharField(max_length=255, verbose_name="Название латиница", null=True, blank=True)
    location = models.CharField(max_length=255, verbose_name="Местоположение")
    # photo = models.ImageField(upload_to="locations", verbose_name="Фото")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
        ordering = ["id"]


class LocationImage(models.Model):
    location = models.ForeignKey(Location, models.SET_NULL, 'images', null=True, blank=True,
                                 verbose_name="фотографии услуги")
    img = models.ImageField(upload_to="locations", verbose_name="Фото")

    def save(self,  *args, **kwargs):
        super(LocationImage, self).save(*args, **kwargs)
        if self.img:
            photo = Image.open(self.img.path)
        if photo.height > 300 or photo.width > 300:
            photo.save(self.img.path, quality=20, optimize=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
