# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 00:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20170422_0002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='confirm_pass',
            new_name='confirmpass',
        ),
    ]
