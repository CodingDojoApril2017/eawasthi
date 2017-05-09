# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=1000)),
                ('weight', models.IntegerField(max_length=45)),
                ('price', models.IntegerField(max_length=45)),
                ('cost', models.IntegerField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]