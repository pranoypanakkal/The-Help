# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='gender',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
