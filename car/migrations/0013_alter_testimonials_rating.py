# Generated by Django 3.2.4 on 2021-07-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0012_testimonials_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
