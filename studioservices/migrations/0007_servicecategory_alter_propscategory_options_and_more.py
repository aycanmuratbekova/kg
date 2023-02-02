# Generated by Django 4.1 on 2023-01-31 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studioservices', '0006_rename_serviceimages_serviceimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория услуг',
                'verbose_name_plural': 'Категории услуг',
            },
        ),
        migrations.AlterModelOptions(
            name='propscategory',
            options={'verbose_name': 'Категория реквизитов', 'verbose_name_plural': 'Категории реквизитов'},
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='studioservices.servicecategory', verbose_name='категория услуг'),
        ),
    ]