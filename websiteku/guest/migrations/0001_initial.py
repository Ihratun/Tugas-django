# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-13 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=50)),
                ('kegiatan', models.TextField()),
            ],
        ),
    ]
