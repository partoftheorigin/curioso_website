# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curiosoblog', '0004_auto_20170824_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
