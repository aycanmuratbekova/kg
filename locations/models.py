from django.db import models
from PIL import Image


class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    url_name = models.CharField(max_length=255, verbose_name="Название латиница")
    location = models.CharField(max_length=255, verbose_name="Местоположение")
    photo = models.ImageField(upload_to="locations", verbose_name="Фото")

    def save(self,  *args, **kwargs):
        super(Location, self).save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            img.save(self.photo.path, quality=20, optimize=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
        ordering = ["id"]
