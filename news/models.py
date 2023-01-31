from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    url_name = models.CharField(max_length=255, verbose_name="Название латиница")
    text = models.TextField(verbose_name="Текст")
    img = models.ImageField(upload_to="news_img/%Y/", null=True, blank=True, verbose_name="Фото")
    news_date = models.DateField(verbose_name="Дата")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"