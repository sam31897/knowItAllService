# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowItAllAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.CharField(default=b'', max_length=200, null=True),
        ),
    ]
