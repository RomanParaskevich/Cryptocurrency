# Generated by Django 3.2.18 on 2023-03-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0023_alter_header_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertising',
            options={'ordering': ['sort'], 'verbose_name': 'Преимущества', 'verbose_name_plural': 'Преимущества'},
        ),
        migrations.AlterModelOptions(
            name='footer',
            options={'ordering': ['sort']},
        ),
        migrations.AlterModelOptions(
            name='inlinefooter',
            options={'ordering': ['sort']},
        ),
        migrations.AlterModelOptions(
            name='maininfo',
            options={'ordering': ['sort'], 'verbose_name': 'Информация', 'verbose_name_plural': 'Информация'},
        ),
        migrations.AlterModelOptions(
            name='socialnetworks',
            options={'ordering': ['sort']},
        ),
        migrations.AddField(
            model_name='advertising',
            name='sort',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='sort',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='inlinefooter',
            name='sort',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='maininfo',
            name='sort',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='socialnetworks',
            name='sort',
            field=models.IntegerField(null=True),
        ),
    ]
