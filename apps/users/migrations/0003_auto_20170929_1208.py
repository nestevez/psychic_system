# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 19:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_access_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='fname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='lname',
            new_name='uname',
        ),
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
    ]