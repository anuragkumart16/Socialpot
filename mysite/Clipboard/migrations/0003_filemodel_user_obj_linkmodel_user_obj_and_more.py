# Generated by Django 5.0.6 on 2024-06-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clipboard', '0002_alter_filemodel_file_alter_linkmodel_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='user_obj',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='linkmodel',
            name='user_obj',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='textmodel',
            name='user_obj',
            field=models.CharField(default='none', max_length=100),
        ),
    ]