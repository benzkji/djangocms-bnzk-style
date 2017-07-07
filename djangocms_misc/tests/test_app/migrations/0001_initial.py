# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-04 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestInlineModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(blank=True, default='', max_length=64)),
                ('field2', models.CharField(blank=True, default='', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field0', models.CharField(blank=True, default='', max_length=64)),
                ('field1', models.CharField(blank=True, default='', max_length=64)),
                ('field2', models.CharField(blank=True, default='', max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='testinlinemodel',
            name='testmodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.TestModel'),
        ),
    ]