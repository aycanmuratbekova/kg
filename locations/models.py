from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    url_name = models.CharField(max_length=255, verbose_name="Название латиница")
    location = models.CharField(max_length=255, verbose_name="Местоположение")
    photo = models.ImageField(upload_to="locations", verbose_name="Фото")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
        ordering = ["id"]
