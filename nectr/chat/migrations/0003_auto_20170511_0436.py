# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-11 04:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20170510_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='initiator_last_read_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 11, 4, 36, 7, 169662, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='recipient_last_read_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 11, 4, 36, 7, 169700, tzinfo=utc)),
        ),
    ]
