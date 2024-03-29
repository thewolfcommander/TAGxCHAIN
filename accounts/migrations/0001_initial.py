# Generated by Django 3.2.6 on 2021-09-01 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TradingAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demo_money', models.DecimalField(decimal_places=2, default=50000.0, max_digits=20)),
                ('real_moeny', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('no_of_trades', models.IntegerField(default=0)),
                ('no_of_sessions', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_spam', models.BooleanField(default=False)),
                ('is_bot_account', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
