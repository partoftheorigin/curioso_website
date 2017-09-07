# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170907_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='additional_information',
            field=models.TextField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='career',
            name='attachment',
            field=models.FileField(upload_to='', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='career',
            name='coding_profile',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='career',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='career',
            name='firstname',
            field=models.CharField(max_length=120, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='career',
            name='github_profile',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='career',
            name='lastname',
            field=models.CharField(max_length=120, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='career',
            name='linkedin_profile',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='firstname',
            field=models.CharField(max_length=120, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='lastname',
            field=models.CharField(max_length=120, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='writeforus',
            name='attachment',
            field=models.FileField(upload_to='', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='writeforus',
            name='category',
            field=models.CharField(max_length=120, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='writeforus',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='writeforus',
            name='firstname',
            field=models.CharField(help_text='Field does not contain blankspace if added, it will be automatically removed', max_length=120, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='writeforus',
            name='lastname',
            field=models.CharField(max_length=120, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='writeforus',
            name='linkedin_profile',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='writeforus',
            name='title',
            field=models.CharField(max_length=120, verbose_name=''),
        ),
    ]