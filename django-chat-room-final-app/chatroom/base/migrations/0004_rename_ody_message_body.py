# Generated by Django 5.0.3 on 2025-03-24 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_room_options_message_ody'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='ody',
            new_name='body',
        ),
    ]
