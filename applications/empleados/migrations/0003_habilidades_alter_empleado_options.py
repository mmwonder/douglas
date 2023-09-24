# Generated by Django 4.2.3 on 2023-08-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_alter_empleado_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ('first_name', 'last_name'), 'verbose_name': 'Empleado', 'verbose_name_plural': 'Personal del la Empresa'},
        ),
    ]
