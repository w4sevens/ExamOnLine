# Generated by Django 3.0.2 on 2021-02-28 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210228_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='is_menu',
        ),
        migrations.AlterUniqueTogether(
            name='menus',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='menus',
            name='url_name',
        ),
        migrations.RemoveField(
            model_name='menus',
            name='url_type',
        ),
    ]