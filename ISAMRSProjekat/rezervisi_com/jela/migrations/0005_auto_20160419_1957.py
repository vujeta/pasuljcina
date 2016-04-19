# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jela', '0004_remove_jelo_restoran'),
    ]

    operations = [
        migrations.AddField(
            model_name='jelo',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='jelo',
            unique_together=set([('naziv', 'slug')]),
        ),
    ]
