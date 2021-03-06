# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-04 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.crypto
import django_lti_login.models
import functools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LTIClient',
            fields=[
                ('key', models.CharField(default=functools.partial(django.utils.crypto.get_random_string, *(), **{'allowed_chars': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'length': 128}), help_text='LTI client service key', max_length=128, primary_key=True, serialize=False, validators=[functools.partial(django_lti_login.models.word_validator, *(), **{'charset': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-', 'length': (6, 128)})])),
                ('secret', models.CharField(default=functools.partial(django.utils.crypto.get_random_string, *(), **{'allowed_chars': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 'length': 128}), help_text='LTI client service secret', max_length=128, validators=[functools.partial(django_lti_login.models.word_validator, *(), **{'charset': None, 'length': (6, 128)})])),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['key'],
            },
        ),
    ]
