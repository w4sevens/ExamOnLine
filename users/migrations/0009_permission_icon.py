# Generated by Django 3.0.2 on 2021-02-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210228_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='icon',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='图标'),
        ),
    ]