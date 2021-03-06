# Generated by Django 3.0.2 on 2021-04-06 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20210404_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='logo名称')),
                ('logo', models.ImageField(default='logo/default.jpg', upload_to='logo/%Y/%m', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'LOGO',
                'verbose_name_plural': 'LOGO',
            },
        ),
        migrations.AddField(
            model_name='units',
            name='logo1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logo1', to='users.Logo', verbose_name='logo1'),
        ),
        migrations.AddField(
            model_name='units',
            name='logo2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logo2', to='users.Logo', verbose_name='logo2'),
        ),
        migrations.AddField(
            model_name='units',
            name='logo3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logo3', to='users.Logo', verbose_name='logo3'),
        ),
    ]
