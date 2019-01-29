# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-23 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App01', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('book', models.ManyToManyField(to='App01.Book')),
            ],
        ),
    ]