# Generated by Django 5.0.6 on 2024-07-31 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clipboard', '0009_rename_user_obj_textmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='Filename',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]