# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-21 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachment', '0003_auto_20190619_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachmentimage',
            name='role',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='role'),
        ),
    ]