# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 23:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0002_auto_20161031_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='past_teams',
            new_name='all_teams',
        ),
    ]
