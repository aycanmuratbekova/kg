# Generated by Django 4.1 on 2023-01-31 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0002_rename_message_contact_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=200, verbose_name='email-почта')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('text', models.TextField(max_length=1000, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Закажите услугу',
                'verbose_name_plural': 'Закажите услуги',
            },
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Свяжитесь с нами', 'verbose_name_plural': 'Свяжитесь с нами'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='email-почта'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.TextField(max_length=1000, verbose_name='Сообщение'),
        ),
    ]
