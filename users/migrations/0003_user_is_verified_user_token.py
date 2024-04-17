# Generated by Django 4.2 on 2024-04-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Подтверждён'),
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.IntegerField(blank=True, null=True, verbose_name='Токен'),
        ),
    ]
