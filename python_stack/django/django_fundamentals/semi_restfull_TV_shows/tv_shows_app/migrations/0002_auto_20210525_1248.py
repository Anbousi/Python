# Generated by Django 2.2.4 on 2021-05-25 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='create_show',
            old_name='r_date',
            new_name='release_date',
        ),
    ]
