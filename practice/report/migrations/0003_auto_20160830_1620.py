# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-30 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('report', '0002_auto_20160830_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createuser',
            name='user_ptr',
        ),
        migrations.AlterField(
            model_name='report',
            name='report_author',
            field=models.CharField(max_length=20, verbose_name='投稿者'),
        ),
        migrations.DeleteModel(
            name='CreateUser',
        ),
    ]
