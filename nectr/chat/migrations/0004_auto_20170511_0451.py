# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-11 04:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20170511_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='initiator_last_read_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 11, 4, 51, 38, 836499, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='recipient_last_read_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 11, 4, 51, 38, 836542, tzinfo=utc)),
        ),
    ]
