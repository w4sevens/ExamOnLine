# encoding: utf-8
# @author: w4dll
# @file: examforms.py
# @time: 2021/2/26 21:44
from exam import models
from django.forms import ModelForm
from exam import models

class QuestionModelForm(ModelForm):

    class Meta:
        model = models.QuestionBank
        fields = ['title', 'question_type', 'answer', 'difficulty', 'score']

    def __new__(cls, *args, **kwargs):
        # cls.base_fields是一个字典：{'name': <django.forms.fields.CharField object at 0x0000013BAA25C0D0>,}
        # dy('打印CustomerForm中的new方法', cls.base_fields)

        # 获取字段对象，设置字段属性
        for field_name in cls.base_fields:
            field_obj = cls.base_fields[field_name]

            # 添加属性
            field_obj.widget.attrs.update({'class': 'form-control'})
        return ModelForm.__new__(cls)


class QuestionInfoModelForm(ModelForm):
    class Meta:
        model = models.QuestionInfo
        fields = ['name', 'applyto']

    def __new__(cls, *args, **kwargs):
        # cls.base_fields是一个字典：{'name': <django.forms.fields.CharField object at 0x0000013BAA25C0D0>,}
        # dy('打印CustomerForm中的new方法', cls.base_fields)

        # 获取字段对象，设置字段属性
        for field_name in cls.base_fields:
            field_obj = cls.base_fields[field_name]

            # 添加属性
            field_obj.widget.attrs.update({'class': 'form-control'})
        return ModelForm.__new__(cls)

class TestPaperModelForm(ModelForm):
    class Meta:
        model = models.TestPaper
        fields = ['paper_name', 'test_time', 'applyto', 'include_qinfo', 'hot_nums']

    def __new__(cls, *args, **kwargs):
        # cls.base_fields是一个字典：{'name': <django.forms.fields.CharField object at 0x0000013BAA25C0D0>,}
        # dy('打印CustomerForm中的new方法', cls.base_fields)

        # 获取字段对象，设置字段属性
        for field_name in cls.base_fields:
            field_obj = cls.base_fields[field_name]

            # 添加属性
            field_obj.widget.attrs.update({'class': 'form-control'})
        return ModelForm.__new__(cls)