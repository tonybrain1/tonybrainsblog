# Generated by Django 2.1.2 on 2018-10-24 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20181021_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
