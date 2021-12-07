# Generated by Django 3.2.9 on 2021-12-05 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrodoc', '0003_auto_20211205_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docente',
            name='administracion',
        ),
        migrations.AlterField(
            model_name='docente',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='registrodoc', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='nodocente',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='registrodoc', verbose_name='Imagen'),
        ),
    ]
