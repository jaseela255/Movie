# Generated by Django 2.2.8 on 2023-04-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=0, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
