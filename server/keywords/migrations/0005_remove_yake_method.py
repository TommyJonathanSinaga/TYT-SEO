# Generated by Django 3.1.4 on 2023-06-07 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0004_auto_20230607_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yake',
            name='method',
        ),
    ]