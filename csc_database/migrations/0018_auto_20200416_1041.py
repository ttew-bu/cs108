# Generated by Django 3.0.4 on 2020-04-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csc_database', '0017_remove_serviceevent_volunteers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
