from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    img = models.ImageField(upload_to="news_img/%Y/", null=True, blank=True, verbose_name="Фото")

    def __str__(self):
        return self.title
