# Generated by Django 3.1.4 on 2023-06-07 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='security_result',
            old_name='pwa_score',
            new_name='result',
        ),
        migrations.AddField(
            model_name='security',
            name='score',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='security_result',
            name='score',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
