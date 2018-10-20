# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-20 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20181020_0833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='user',
            new_name='posted_by',
        ),
        migrations.AlterField(
            model_name='alert',
            name='neighbor_hood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='app.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='business',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='app.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='app.Neighborhood'),
        ),
    ]