# Generated by Django 3.2.6 on 2021-09-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_fee_pay_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='trans_id',
            field=models.IntegerField(default=1, verbose_name='Transaction ID'),
        ),
        migrations.AddField(
            model_name='gym',
            name='trans',
            field=models.IntegerField(default=1, verbose_name='Transaction Number'),
        ),
    ]
