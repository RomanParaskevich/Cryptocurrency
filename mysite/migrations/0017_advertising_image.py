# Generated by Django 3.2.18 on 2023-03-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_advertising_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertising',
            name='image',
            field=models.FileField(blank=True, upload_to='uploads/', verbose_name='Иконка'),
        ),
    ]