# Generated by Django 5.0.1 on 2024-01-29 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlet',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outlet',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]