from django.contrib import admin
from exam.models import QuestionBank, TestPaper, Record
from kingadmin.sites import site
from kingadmin.admin_base import BaseKingAdmin


# Register your models here.
# 题库表
class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "question_type", "answer", "difficulty", "score")
    # 根据科目 专业去搜索
    search_fields = ("question_type", "title")
    # 过滤器  根据题科目的名称  以及专业的名称  题目名称
    list_filter = ("difficulty", "title")
    # 按照序号排列
    ordering = ("id",)
    list_per_page = 10
    # actions = ["export_as_excel", ]
site.register(QuestionBank, QuestionBankAdmin)
#
#
# # 试卷
# @admin.register(TestPaper)
# class TestPaperAdmin(admin.ModelAdmin):
#     def show_question(self, obj):
#         return [exam_q.title for exam_q in obj.exam_questions.all()]
#
#     list_display = ("id", "name", "test_time", "addtime", "create_person")
#
#     # filter_horizontal = ("exam_questions",)
#
#     # 根据科目 专业去搜索
#     # search_fields = ("tid", "zhuanye", "course")
#     # # 过滤器  根据题科目的名称  以及专业的名称  题目名称
#     # list_filter = ("tid", "zhuanye", "course")
#     # 按照序号排列
#     list_per_page = 10
#     ordering = ['id']
#     # actions = ["export_as_excel", ]
#
# # 成绩表
# @admin.register(Record)
# class RecordAdmin(admin.ModelAdmin):
#     list_display = ("id", "papername", "test_time", "userid", 'grade')
#     # 根据科目 专业去搜索
#     search_fields = ("papername", "userid")
#     # 过滤器  根据题科目的名称  以及专业的名称  题目名称
#     # list_filter = ("xuehao",)
#     # 按照序号排列
#     # list_per_page = 10
#     # 按照成绩降序排列
#     ordering = ['-grade']
#     # actions = ["export_as_excel", ]
#
#
#
# # 站点名称
# admin.site.site_header = '在线考试系统'
#
# # 网页标题
# admin.site.site_title = '在线考试系统后台'