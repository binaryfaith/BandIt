# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandsApp', '0010_auto_20171022_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='totalPrice',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]