# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-22 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandsApp', '0009_merge_20171022_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='bandsApp.User'),
        ),
    ]
