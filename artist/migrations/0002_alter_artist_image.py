# Generated by Django 4.1.3 on 2022-12-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='artist/'),
        ),
    ]
