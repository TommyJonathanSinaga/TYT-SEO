# Generated by Django 3.0.6 on 2023-06-07 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extractor', '0002_auto_20230707_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractor',
            name='task_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
