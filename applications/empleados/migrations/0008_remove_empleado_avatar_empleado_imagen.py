# Generated by Django 4.2.3 on 2023-09-03 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0007_empleado_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='avatar',
        ),
        migrations.AddField(
            model_name='empleado',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='empleados'),
        ),
    ]
