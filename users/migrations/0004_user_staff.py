# Generated by Django 3.1.3 on 2020-11-16 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201113_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]