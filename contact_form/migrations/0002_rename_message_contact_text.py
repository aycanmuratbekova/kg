# Generated by Django 4.1 on 2023-01-31 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='text',
        ),
    ]
