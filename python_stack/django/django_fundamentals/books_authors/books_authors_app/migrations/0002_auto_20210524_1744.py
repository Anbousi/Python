# Generated by Django 2.2.4 on 2021-05-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='author', to='books_authors_app.Book'),
        ),
    ]
