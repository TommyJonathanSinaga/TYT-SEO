# Generated by Django 3.0.6 on 2023-06-07 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lighthouse', '0007_auto_20230607_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lighthouse_result',
            name='performance_score',
            field=models.CharField(max_length=10),
        ),
    ]
