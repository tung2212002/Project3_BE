# Generated by Django 4.2.4 on 2023-09-01 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='user_post/blank-picture.png', upload_to='thumbnails'),
        ),
    ]