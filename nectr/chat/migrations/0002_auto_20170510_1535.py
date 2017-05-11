# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 15:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='initiator_last_read_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 10, 15, 35, 17, 124029, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='conversation',
            name='recipient_last_read_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 10, 15, 35, 17, 124083, tzinfo=utc)),
        ),
    ]
