# Generated by Django 3.2.13 on 2022-11-16 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='released_date',
            field=models.DateField(),
        ),
    ]
