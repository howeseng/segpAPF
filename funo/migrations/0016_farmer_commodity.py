# Generated by Django 3.0.3 on 2020-04-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funo', '0015_farmer_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='commodity',
            field=models.CharField(max_length=200, null=True),
        ),
    ]