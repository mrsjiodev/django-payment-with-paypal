# Generated by Django 2.2 on 2020-09-29 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200929_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='role',
            field=models.CharField(blank=True, choices=[('Monthly', 'monthly'), ('Yearly', 'yearly')], max_length=150, null=True),
        ),
    ]
