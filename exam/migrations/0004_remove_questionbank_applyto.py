# Generated by Django 3.0.2 on 2021-02-25 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20210225_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionbank',
            name='applyto',
        ),
    ]
