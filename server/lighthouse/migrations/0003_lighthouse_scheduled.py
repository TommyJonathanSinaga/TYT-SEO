# Generated by Django 3.0.6 on 2023-06-07 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lighthouse', '0002_auto_20230607_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='lighthouse',
            name='scheduled',
            field=models.BooleanField(default=False),
        ),
    ]
