# Generated by Django 3.0.2 on 2021-02-25 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': '考试记录', 'verbose_name_plural': '考试记录'},
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='question_type',
            field=models.IntegerField(choices=[(0, '单选题'), (1, '多选题'), (2, '判断题'), (3, '填空题'), (4, '问答题')], verbose_name='题目类型'),
        ),
    ]
