# Generated by Django 3.2 on 2021-11-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_fee_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='trans',
            field=models.CharField(default=1, max_length=100, verbose_name='Transaction Number'),
        ),
    ]
