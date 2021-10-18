# Generated by Django 3.2.6 on 2021-10-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0002_alter_tradingday_charges'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradingday',
            name='amount_used',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Trading amount used', max_digits=20),
        ),
        migrations.AddField(
            model_name='tradingday',
            name='pnl_percentage',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Percentage of Profit and loss', max_digits=5),
        ),
    ]
