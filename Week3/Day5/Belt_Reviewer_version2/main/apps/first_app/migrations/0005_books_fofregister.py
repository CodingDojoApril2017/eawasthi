# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20170423_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='fOfRegister',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first_app.Register'),
        ),
    ]
