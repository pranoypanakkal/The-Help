# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20170314_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='skill_1',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='skill_2',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='skill_3',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='skill_4',
        ),
        migrations.AddField(
            model_name='worker',
            name='skills',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
