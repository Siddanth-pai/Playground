# Generated by Django 2.0.8 on 2018-10-12 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181012_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='videoFile',
            new_name='videofile',
        ),
        migrations.AddField(
            model_name='video',
            name='views_count',
            field=models.IntegerField(default=170),
        ),
    ]