# Generated by Django 3.0.2 on 2021-04-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20210404_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='units',
            name='uname2',
            field=models.CharField(default='', max_length=32, verbose_name='二级单位'),
        ),
        migrations.AlterField(
            model_name='units',
            name='unit_name',
            field=models.CharField(max_length=32, verbose_name='单位简称'),
        ),
    ]