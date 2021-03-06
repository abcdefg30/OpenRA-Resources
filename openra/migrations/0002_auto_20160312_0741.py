# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 07:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openra', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CrashReports',
        ),
        migrations.RemoveField(
            model_name='mods',
            name='user',
        ),
        migrations.RemoveField(
            model_name='palettes',
            name='user',
        ),
        migrations.RemoveField(
            model_name='units',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='lints',
            options={'verbose_name_plural': 'Lints'},
        ),
        migrations.AlterModelOptions(
            name='maps',
            options={'verbose_name_plural': 'Maps'},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name_plural': 'Ratings'},
        ),
        migrations.AlterModelOptions(
            name='replayplayers',
            options={'verbose_name_plural': 'ReplayPlayers'},
        ),
        migrations.AlterModelOptions(
            name='replays',
            options={'verbose_name_plural': 'Replays'},
        ),
        migrations.AlterModelOptions(
            name='reports',
            options={'verbose_name_plural': 'Reports'},
        ),
        migrations.AlterModelOptions(
            name='screenshots',
            options={'verbose_name_plural': 'Screenshots'},
        ),
        migrations.AlterModelOptions(
            name='unsubscribecomments',
            options={'verbose_name_plural': 'Unsubscribed From Comments'},
        ),
        migrations.DeleteModel(
            name='Mods',
        ),
        migrations.DeleteModel(
            name='Palettes',
        ),
        migrations.DeleteModel(
            name='Units',
        ),
    ]
