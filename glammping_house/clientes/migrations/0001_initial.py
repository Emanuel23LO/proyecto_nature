# Generated by Django 5.0 on 2023-12-05 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('document', models.CharField(max_length=20, unique=True)),
                ('nationality', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
