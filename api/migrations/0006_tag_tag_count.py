# Generated by Django 4.2.4 on 2023-09-04 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tag_count',
            field=models.IntegerField(default=0),
        ),
    ]
