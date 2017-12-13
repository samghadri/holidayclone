# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]
