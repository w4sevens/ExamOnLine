# Generated by Django 3.0.2 on 2021-03-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_auto_20210311_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testpaper',
            name='paper_name',
            field=models.CharField(max_length=40, verbose_name='试卷名称'),
        ),
    ]
