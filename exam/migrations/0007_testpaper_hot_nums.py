# Generated by Django 3.0.2 on 2021-02-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_auto_20210226_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='testpaper',
            name='hot_nums',
            field=models.IntegerField(default=0, verbose_name='热度'),
        ),
    ]