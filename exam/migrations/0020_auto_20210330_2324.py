# Generated by Django 3.0.2 on 2021-03-30 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0019_auto_20210330_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testpaper',
            name='blongs_to_paper',
        ),
        migrations.AddField(
            model_name='testpaper',
            name='include_qinfo',
            field=models.ManyToManyField(blank=True, default='', null=True, to='exam.QuestionInfo', verbose_name='包含题库'),
        ),
    ]
