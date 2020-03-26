# Generated by Django 3.0.4 on 2020-03-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True)),
                ('last_name', models.TextField(blank=True)),
                ('city', models.TextField(blank=True)),
                ('email_address', models.TextField(blank=True)),
                ('profile_image_url', models.URLField(blank=True)),
            ],
        ),
    ]
