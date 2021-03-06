# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 18:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=8)),
                ('programme', models.CharField(choices=[('Btech', 'Btech'), ('Mtech', 'Mtech'), ('Msc', 'Msc'), ('Ma', 'Ma'), ('Phd', 'Phd'), ('Alumni', 'Alumni')], default='Btech', max_length=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
