# Generated by Django 5.0 on 2023-12-06 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_rename_valor_servicio_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='image',
        ),
        migrations.AddField(
            model_name='servicio',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]