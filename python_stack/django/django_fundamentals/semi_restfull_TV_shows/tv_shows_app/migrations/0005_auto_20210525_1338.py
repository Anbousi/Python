# Generated by Django 2.2.4 on 2021-05-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0004_auto_20210525_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='release_date',
            field=models.DateField(),
        ),
    ]
