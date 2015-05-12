# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50, blank=True)),
                ('role', models.CharField(max_length=50, blank=True)),
                ('office', models.CharField(max_length=50, blank=True)),
                ('mobile', models.CharField(max_length=50, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('url', models.URLField(blank=True)),
                ('next_call', models.DateField(blank=True)),
                ('note', models.TextField(blank=True)),
                ('introduced_by', models.CharField(max_length=50, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_in', models.BooleanField(default=False)),
                ('email_out', models.BooleanField(default=False)),
                ('email_linkedin', models.BooleanField(default=False)),
                ('call_in', models.BooleanField(default=False)),
                ('call_out', models.BooleanField(default=False)),
                ('voice_mail', models.BooleanField(default=False)),
                ('message', models.BooleanField(default=False)),
                ('no_message', models.BooleanField(default=False)),
                ('no_answer', models.BooleanField(default=False)),
                ('meeting', models.BooleanField(default=False)),
                ('write_up', models.TextField(blank=True)),
                ('contacted_at', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ForeignKey(to='tocall.Contact')),
            ],
        ),
    ]
