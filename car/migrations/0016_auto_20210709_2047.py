# Generated by Django 3.2.4 on 2021-07-09 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0015_booking_carid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='dropLocation',
            field=models.CharField(choices=[('Ahmedabad', (('ahmrailway', 'Railway Station'), ('ahmairport', 'Ahmedabad Airport')))], max_length=128),
        ),
        migrations.AlterField(
            model_name='booking',
            name='pickupLocation',
            field=models.CharField(choices=[('Ahmedabad', (('ahmrailway', 'Railway Station'), ('ahmairport', 'Ahmedabad Airport')))], max_length=128),
        ),
    ]
