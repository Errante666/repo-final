# Generated by Django 3.2.9 on 2021-11-25 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrodoc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidad',
            field=models.ManyToManyField(to='registrodoc.Habilidad'),
        ),
    ]
