# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 17:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_auto_20170515_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='initiator_last_read_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 15, 17, 59, 53, 934020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='recipient_last_read_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 15, 17, 59, 53, 934072, tzinfo=utc)),
        ),
    ]
