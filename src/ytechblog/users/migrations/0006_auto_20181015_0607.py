# Generated by Django 2.1.2 on 2018-10-15 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_advertimages_thumb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdvertImages',
            new_name='Advert',
        ),
    ]