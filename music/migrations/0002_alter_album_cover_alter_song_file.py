# Generated by Django 4.1.3 on 2022-12-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(upload_to='album_cover'),
        ),
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(upload_to='album'),
        ),
    ]
