# Generated by Django 5.0.4 on 2024-04-06 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_player', '0003_song_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='order',
        ),
    ]
