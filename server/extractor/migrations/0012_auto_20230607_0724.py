# Generated by Django 3.1.4 on 2020-06-07 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extractor', '0011_auto_20230607_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extractor',
            old_name='Org',
            new_name='org',
        ),
    ]