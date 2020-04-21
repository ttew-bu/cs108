# Generated by Django 3.0.5 on 2020-04-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csc_database', '0024_remove_serviceevent_volunteers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypartner',
            name='cp_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='communitypartner',
            name='cp_type',
            field=models.CharField(choices=[('Food Justice', 'Food'), ('LGBTQ', 'Lgbtq'), ('Education', 'Education'), ('Racial Equity', 'Equity'), ('Empowerment of women', 'Womens')], max_length=100),
        ),
    ]
