# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_users_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
