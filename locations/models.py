from PIL import Image
from io import BytesIO
from django.core.files import File
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    url_name = models.CharField(max_length=255, verbose_name="Название латиница", null=True, blank=True)
    location = models.CharField(max_length=255, verbose_name="Местоположение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
        ordering = ["id"]


def compress(image):
    im = Image.open(image)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


class LocationImage(models.Model):
    location = models.ForeignKey(Location, models.SET_NULL, 'images', null=True, blank=True,
                                 verbose_name="фотографии услуги")
    img = models.ImageField(upload_to="locations", verbose_name="Фото")

    def save(self, *args, **kwargs):
        new_image = compress(self.img)
        self.img = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
