# Generated by Django 5.0.6 on 2024-05-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Linkmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Link', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Textmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.TextField(max_length=1000)),
            ],
        ),
    ]
