# Generated by Django 3.0.6 on 2023-06-07 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lighthouse', '0004_auto_20230607_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lighthouse_result',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lighthouse', to='lighthouse.Lighthouse'),
        ),
    ]
