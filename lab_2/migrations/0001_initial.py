# Generated by Django 3.2.7 on 2021-09-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_to', models.CharField(max_length=30)),
                ('note_from', models.CharField(max_length=30)),
                ('note_title', models.CharField(max_length=30)),
                ('note_message', models.TextField()),
            ],
        ),
    ]
