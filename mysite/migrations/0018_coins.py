# Generated by Django 3.2.18 on 2023-03-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_advertising_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=124, verbose_name='Заголовок')),
                ('tag', models.CharField(max_length=124)),
                ('description', models.CharField(max_length=124, verbose_name='Описание')),
                ('image', models.FileField(upload_to='uploads/', verbose_name='Иконка')),
                ('url', models.CharField(blank=True, max_length=124)),
            ],
            options={
                'verbose_name': 'Монеты',
                'verbose_name_plural': 'Монеты',
            },
        ),
    ]
