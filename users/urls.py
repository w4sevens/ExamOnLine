# encoding: utf-8
# @author: w4dll
# @file: urls.py
# @time: 2021/3/12 23:50
from django.contrib import admin
from django.urls import path, include
from users import views
app_name = 'user'

urlpatterns = [
    # 账户中心
    path('info/', views.userinfo, name='userinfo'),
    path('info/<str:ustr>/detail/', views.user_unit_detail, name='user_unit_detail'),

    # 用户列表
    path('list/', views.userlist, name='userlist'),
    path('edit/<int:uid>/', views.useredit, name='useredit'),
    path('delete/<int:uid>/', views.userdelete, name='userdelete'),
    path('add/', views.useradd, name='useradd'),

    # 个人中心
    path('showme/', views.showme, name='showme'),
    path('img_upload/', views.img_upload, name='img_upload'),
    path('save/', views.usersave, name='usersave'),
    path('change_pwd/', views.change_pwd, name='change_pwd'),

    # 设置界面
    path('config/', views.config, name='config'),
    path('config/unit/list/', views.unitlist, name='unitlist'),
    path('config/unit/add/', views.unitadd, name='unitadd'),
    path('config/unit/<int:uid>/edit/', views.edit_unit, name='edit_unit'),
    path('config/unit/<int:uid>/delete/', views.delete_unit, name='delete_unit'),

]