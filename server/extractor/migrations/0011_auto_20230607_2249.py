# Generated by Django 3.1.4 on 2023-06-07 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0001_initial'),
        ('extractor', '0010_extractor_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractor',
            name='Org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extractor', to='org.website'),
        ),
    ]
