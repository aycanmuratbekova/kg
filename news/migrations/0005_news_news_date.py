# Generated by Django 4.1 on 2023-01-31 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_url_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_date',
            field=models.DateField(auto_now_add=True, default='1996-12-12'),
            preserve_default=False,
        ),
    ]
