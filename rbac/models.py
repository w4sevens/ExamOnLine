from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField('角色名称', max_length=64, unique=True)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name


class Permission(models.Model):
    """
    权限表
    """
    url = models.CharField(verbose_name='含正则的URL', max_length=128)
    title = models.CharField(verbose_name='权限', max_length=32)
    is_menu = models.ForeignKey('Menus', verbose_name='是否菜单', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name


class Menus(models.Model):
    """菜单"""
    title = models.CharField(max_length=32, verbose_name='菜单', default='')
    icon = models.CharField(max_length=32, verbose_name='图标', null=True, blank=True)
    sequence = models.IntegerField('菜单序号', default=0)
    layer_choice = ((0, '一级菜单'), (1, '二级菜单'))
    layer = models.IntegerField('菜单级别', choices=layer_choice, default=0)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name