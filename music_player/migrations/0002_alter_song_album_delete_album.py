# Generated by Django 5.0.4 on 2024-04-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
