# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-02 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20171202_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=255, unique=True)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('section', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
    ]
