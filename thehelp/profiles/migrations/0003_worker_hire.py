# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_worker_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='hire',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]