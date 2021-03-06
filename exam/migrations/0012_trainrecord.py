# Generated by Django 3.0.2 on 2021-03-16 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0011_testpaper_applyto'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_type', models.CharField(max_length=128, verbose_name='训练方式')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.QuestionInfo', verbose_name='训练内容')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='姓名')),
                ('wrong', models.ManyToManyField(to='exam.QuestionBank', verbose_name='错题')),
            ],
            options={
                'verbose_name': '训练记录',
                'verbose_name_plural': '训练记录',
            },
        ),
    ]
