# Generated by Django 4.2.3 on 2023-08-31 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
    ]
