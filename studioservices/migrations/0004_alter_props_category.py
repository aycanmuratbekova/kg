# Generated by Django 4.1 on 2022-11-09 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studioservices', '0003_props_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='props',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='props', to='studioservices.propscategory', verbose_name='категория реквизита'),
        ),
    ]