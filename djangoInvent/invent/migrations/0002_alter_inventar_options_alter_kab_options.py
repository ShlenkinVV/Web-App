# Generated by Django 4.1.7 on 2023-04-01 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invent', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventar',
            options={'verbose_name': 'Инвентарь', 'verbose_name_plural': 'Инвентарь'},
        ),
        migrations.AlterModelOptions(
            name='kab',
            options={'verbose_name': 'Кабинет', 'verbose_name_plural': 'Кабинеты'},
        ),
    ]
