# Generated by Django 2.2.4 on 2021-05-25 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0005_auto_20210525_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shows',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
