from django.db import models
from django.contrib.auth.models import AbstractUser
from rbac.models import Role

# Create your models here.

class Logo(models.Model):
    name = models.CharField('logo名称', max_length=64)
    logo = models.ImageField('logo', upload_to='logo/%Y/%m', default='logo/default.jpg', max_length=100)

    # 修改显示的表的名字
    class Meta:
        verbose_name = 'LOGO'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 单位信息
class Units(models.Model):

    unit_full_name = models.CharField('单位全称', max_length=100)
    unit_name = models.CharField('单位简称', max_length=32)
    uname2 = models.CharField('二级单位', max_length=32, default='')

    logo1 = models.ForeignKey(Logo, related_name='logo1', verbose_name='logo1', blank=True, null=True, on_delete=models.CASCADE)
    logo2 = models.ForeignKey(Logo, related_name='logo2', verbose_name='logo2', blank=True, null=True, on_delete=models.CASCADE)
    logo3 = models.ForeignKey(Logo, related_name='logo3', verbose_name='logo3', blank=True, null=True, on_delete=models.CASCADE)

    # 修改显示的表的名字
    class Meta:
        verbose_name = '单位信息表'
        verbose_name_plural = verbose_name
        unique_together = ('uname2', 'unit_name')

    def __str__(self):
        return self.unit_name + '/' + self.uname2


# 用户表
class UserProfile(AbstractUser):

    nick_name = models.CharField('姓名', max_length=50, default='', null=True)
    birthday = models.DateField('生日', null=True, blank=True)
    idcard = models.CharField('身份证号', default='', max_length=18, null=True, blank=True)
    GENDER_CHOICES = (('male', '男'), ('female', '女'), ('unknown', '不详'))
    gender = models.CharField('性别', max_length=10, choices=GENDER_CHOICES, default='unknow')

    address = models.CharField('地址', max_length=100, default='', null=True, blank=True)
    mobile = models.CharField('手机号', max_length=11, null=True, blank=True)
    image = models.ImageField('头像', upload_to='image/%Y/%m', default='image/default.jpg', max_length=100)
    unit = models.ForeignKey(Units, verbose_name='单位', on_delete=models.SET_NULL, null=True, default='')
    role = models.ManyToManyField(Role, blank=True, null=True, verbose_name='拥有的所有角色')

    # 注意：由于继承了AbstractUser，注册时间字段为date_joined


    def getUserRoleName(self):
        roles = self.role.all()
        rlist = []
        for r in roles:
            rlist.append(r.name)

        if '超级管理员' in rlist:
            return '超级管理员'
        elif '管理员' in rlist:
            return '管理员'
        elif '一般用户' in rlist:
            return '一般用户'
        else:
            return ''

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.nick_name
