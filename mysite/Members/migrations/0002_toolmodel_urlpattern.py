# Generated by Django 5.0.6 on 2024-05-26 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolmodel',
            name='Urlpattern',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
