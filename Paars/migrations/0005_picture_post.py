# Generated by Django 2.0.1 on 2018-12-12 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Paars', '0004_auto_20181212_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='post',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='Paars.Post'),
        ),
    ]
