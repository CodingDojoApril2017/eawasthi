# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 09:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20170423_0917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='authorName',
        ),
        migrations.RemoveField(
            model_name='author',
            name='addnewauthor',
        ),
        migrations.RemoveField(
            model_name='author',
            name='authorlist',
        ),
    ]
