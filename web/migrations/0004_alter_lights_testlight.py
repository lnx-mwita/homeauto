# Generated by Django 4.0.5 on 2022-06-08 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_lights_testlight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lights',
            name='testlight',
            field=models.BooleanField(),
        ),
    ]
