# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
        ('tutor', '0002_tutor_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='skills',
            field=models.ManyToManyField(to='skills.Skills'),
        ),
    ]
