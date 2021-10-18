# Generated by Django 3.2.6 on 2021-10-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_platformsettingsenabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformsettingsenabled',
            name='analysis',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='platformsettingsenabled',
            name='fundamentals',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='platformsettingsenabled',
            name='screeners',
            field=models.BooleanField(default=True),
        ),
    ]
