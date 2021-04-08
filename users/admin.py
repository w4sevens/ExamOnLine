from django.contrib import admin
from users import models

# 用户信息
@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'nick_name', 'is_superuser',
                    'birthday', 'gender', 'address', 'mobile', 'image']

# 单位信息
@admin.register(models.Units)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ("unit_full_name", "unit_name", "uname2", 'logo1', 'logo2', 'logo3')

    # 按照学号降序排列
    ordering = ("id",)

@admin.register(models.Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ("name", "logo")
#
# @admin.register(models.Menus)
# class MenusAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'sequence', 'layer', 'icon')
#     list_editable = ('title', 'icon', 'sequence', 'layer')
#     ordering = ['sequence']  # 按照主键从低到高
#
# @admin.register(models.Permission)
# class PermissionAdmin(admin.ModelAdmin):
#     list_display = ['pk', 'title', 'is_menu', 'url']
#     list_editable = ['title', 'url', 'is_menu']
#     ordering = ['pk']  # 按照主键从低到高
