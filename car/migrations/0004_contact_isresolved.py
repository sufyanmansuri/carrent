# Generated by Django 3.2.4 on 2021-07-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_alter_contact_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='isResolved',
            field=models.BooleanField(default=False),
        ),
    ]
