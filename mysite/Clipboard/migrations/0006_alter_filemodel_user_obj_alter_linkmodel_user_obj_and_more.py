# Generated by Django 5.0.6 on 2024-07-06 11:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clipboard', '0005_filemodel_filename'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='user_obj',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='linkmodel',
            name='user_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='textmodel',
            name='user_obj',
            field=models.CharField(max_length=100),
        ),
    ]
