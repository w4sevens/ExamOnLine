# Generated by Django 3.0.2 on 2021-03-14 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210306_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='usertype',
        ),
    ]
