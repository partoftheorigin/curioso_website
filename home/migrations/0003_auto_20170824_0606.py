# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 06:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_writeforus'),
    ]

    operations = [
        migrations.AddField(
            model_name='writeforus',
            name='content',
            field=models.TextField(default=datetime.datetime(2017, 8, 24, 6, 6, 6, 641888, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='writeforus',
            name='Linkedin_Profile',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
