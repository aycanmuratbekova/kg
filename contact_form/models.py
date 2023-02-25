from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    email = models.EmailField(max_length=200, verbose_name='email-почта')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    text = models.TextField(max_length=1000, verbose_name='Сообщение')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Прозьбы обратной связи"
        verbose_name_plural = "Прозьбы обратной связи"


class OrderService(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    email = models.EmailField(max_length=200, verbose_name='email-почта')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    text = models.TextField(max_length=1000, verbose_name='Сообщение')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Заказали услугу"
        verbose_name_plural = "Заказали услугу"
