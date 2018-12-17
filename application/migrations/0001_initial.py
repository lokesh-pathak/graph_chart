# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-17 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('workclass', models.CharField(blank=True, max_length=255, null=True)),
                ('fnlwgt', models.CharField(blank=True, max_length=255, null=True)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('education_num', models.IntegerField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('relationship', models.CharField(blank=True, max_length=255, null=True)),
                ('race', models.CharField(blank=True, max_length=255, null=True)),
                ('sex', models.CharField(blank=True, max_length=255, null=True)),
                ('capital_gain', models.IntegerField(blank=True, null=True)),
                ('capital_loss', models.IntegerField(blank=True, null=True)),
                ('hours_per_week', models.IntegerField(blank=True, null=True)),
                ('native_country', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'user_data',
            },
        ),
    ]