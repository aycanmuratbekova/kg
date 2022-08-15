# Generated by Django 4.1 on 2022-08-15 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0003_alter_personinmovie_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personinmovie',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='persons', to='art.movie'),
        ),
        migrations.AlterField(
            model_name='personinmovie',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='art.person'),
        ),
    ]
