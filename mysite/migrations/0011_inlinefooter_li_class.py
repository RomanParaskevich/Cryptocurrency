# Generated by Django 3.2.18 on 2023-03-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_auto_20230305_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='inlinefooter',
            name='li_class',
            field=models.CharField(blank=True, max_length=124),
        ),
    ]