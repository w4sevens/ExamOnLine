from django.contrib import admin
from rbac import models

# Register your models here.
@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", )

@admin.register(models.Menus)
class MenusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sequence', 'layer', 'icon')
    list_editable = ('title', 'icon', 'sequence', 'layer')
    ordering = ['sequence']  # 按照主键从低到高

@admin.register(models.Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'is_menu', 'url']
    list_editable = ['title', 'url', 'is_menu']
    ordering = ['url']  # 按照主键从低到高
    # list_per_page = 10