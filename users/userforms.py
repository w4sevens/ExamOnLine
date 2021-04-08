# encoding: utf-8
# @author: w4dll
# @file: userforms.py
# @time: 2021/3/4 22:51
from django import forms
from users import models
from utils.utils import dy
from utils.str_check import is_login_name
from django.forms import ValidationError


class UserProfileForm(forms.Form):
    username = forms.CharField(min_length=3, label="用户名")
    pwd = forms.CharField(min_length=6, label="密码")

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_username(self):
        uname = self.cleaned_data.get('username')
        if is_login_name(uname):
            return uname
        else:
            raise ValidationError("用户名不合法！")


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['nick_name', 'birthday', 'gender', 'address', 'mobile', 'image', 'unit']


    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

from django.forms import widgets as wid
class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = '__all__'
        # exclude = ['password', 'is_superuser', 'groups', 'user_permissions', 'email', 'is_active',
        #            'is_staff']


    def __init__(self, *args, **kwargs):
        super(UserProfileModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            wd = self.fields[field].widget
            if isinstance(wd, wid.RadioChoiceInput):
                wd.attrs.update({
                    'class': 'form-inline',
                })
            else:
                wd.attrs.update({
                    'class': 'form-control',
                })