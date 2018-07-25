# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-24 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finterest_app', '0002_auto_20180724_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='favorite_image',
            field=models.ImageField(blank=True, upload_to='favorite_image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(blank=True, default='null', upload_to='profile_image'),
            preserve_default=False,
        ),
    ]