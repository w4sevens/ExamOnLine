# Generated by Django 3.0.2 on 2021-02-28 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210228_1353'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='menus',
            unique_together={('title', 'url_name')},
        ),
        migrations.RemoveField(
            model_name='menus',
            name='name',
        ),
    ]
