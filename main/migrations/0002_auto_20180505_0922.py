# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-05 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='\u0426\u0435\u043d\u0430'),
        ),
    ]
