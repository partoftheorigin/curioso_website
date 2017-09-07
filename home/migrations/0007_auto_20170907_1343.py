# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170907_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=120)),
                ('lastname', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('attachment', models.FileField(upload_to='')),
                ('linkedin_profile', models.CharField(blank=True, max_length=120, null=True)),
                ('github_profile', models.CharField(blank=True, max_length=120, null=True)),
                ('coding_profile', models.CharField(blank=True, max_length=120, null=True)),
                ('additional_information', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='Feedback',
            new_name='feedback',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='firstname',
            field=models.CharField(max_length=120, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='lastname',
            field=models.CharField(max_length=120, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='writeforus',
            name='attachment',
            field=models.FileField(upload_to=''),
        ),
    ]