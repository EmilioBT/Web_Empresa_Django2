# Generated by Django 5.0.6 on 2024-06-27 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 27, 9, 45, 55, 420852, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicación'),
        ),
    ]
