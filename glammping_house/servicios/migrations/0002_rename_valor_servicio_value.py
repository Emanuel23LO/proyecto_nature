# Generated by Django 5.0 on 2023-12-05 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='valor',
            new_name='value',
        ),
    ]