# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20170309_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='city',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='password',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='state',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
