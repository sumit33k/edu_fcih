# Generated by Django 2.0.3 on 2018-03-27 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_system', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='creation_time',
            new_name='created',
        ),
    ]
