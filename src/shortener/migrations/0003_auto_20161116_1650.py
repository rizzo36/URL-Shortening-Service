# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20161115_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='KirrURLManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='kirrurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
