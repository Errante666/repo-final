# Generated by Django 3.2.9 on 2021-12-05 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrodoc', '0004_auto_20211205_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrodoc.materia'),
        ),
    ]
