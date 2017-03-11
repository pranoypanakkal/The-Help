# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_worker_hire'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='skills',
        ),
        migrations.AddField(
            model_name='worker',
            name='skill_1',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='skill_2',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='skill_3',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='skill_4',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
