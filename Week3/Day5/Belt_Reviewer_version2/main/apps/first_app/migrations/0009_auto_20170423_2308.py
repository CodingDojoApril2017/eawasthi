# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_auto_20170423_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('review', models.TextField(max_length=1000)),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fUsers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first_app.Users')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='authorAndBook',
            field=models.ManyToManyField(related_name='author_related', to='first_app.Books'),
        ),
    ]
