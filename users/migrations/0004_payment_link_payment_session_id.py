# Generated by Django 4.2.13 on 2024-08-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='link',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='ссылка на оплату'),
        ),
        migrations.AddField(
            model_name='payment',
            name='session_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='id сессии'),
        ),
    ]
