# Generated by Django 3.0.6 on 2023-06-07 22:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('YAKE', 'Yake')], max_length=20)),
                ('text', models.TextField(blank=True, null=True)),
                ('result', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('language', models.CharField(max_length=5)),
                ('ngram', models.IntegerField()),
                ('number', models.IntegerField()),
                ('status_job', models.CharField(blank=True, max_length=20, null=True)),
                ('task_id', models.CharField(blank=True, max_length=50, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]