# Generated by Django 3.2.18 on 2023-03-11 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0024_auto_20230311_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertising',
            name='sort',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='sort',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='header',
            name='sort',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inlinefooter',
            name='sort',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maininfo',
            name='sort',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socialnetworks',
            name='sort',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]