# Generated by Django 4.1 on 2022-09-29 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_alter_mywatchlist_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='release_date',
            field=models.CharField(max_length=225),
        ),
    ]
