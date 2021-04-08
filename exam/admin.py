from django.contrib import admin
from exam import models

# Register your models here.
# 题库表
@admin.register(models.QuestionBank)
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

# 试卷
@admin.register(models.TestPaper)
class TestPaperAdmin(admin.ModelAdmin):
    def show_question(self, obj):
        return [exam_q.title for exam_q in obj.exam_questions.all()]

    list_display = ("id", "paper_name", "test_time", "add_time", "create_person", 'hot_nums')

    # filter_horizontal = ("exam_questions",)

    # 根据科目 专业去搜索
    # search_fields = ("tid", "zhuanye", "course")
    # # 过滤器  根据题科目的名称  以及专业的名称  题目名称
    # list_filter = ("tid", "zhuanye", "course")
    # 按照序号排列
    list_per_page = 10
    ordering = ['id']
    # actions = ["export_as_excel", ]

# 成绩表
@admin.register(models.Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "papername", "test_time", "userid", 'grade')
    # 根据科目 专业去搜索
    search_fields = ("papername", "userid")
    # 过滤器  根据题科目的名称  以及专业的名称  题目名称
    # list_filter = ("xuehao",)
    # 按照序号排列
    # list_per_page = 10
    # 按照成绩降序排列
    ordering = ['-grade']
    # actions = ["export_as_excel", ]

@admin.register(models.WrongRecord)
class WrongRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "paper", "question", 'error_times')

@admin.register(models.QuestionInfo)
class QuestionInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_person', 'add_time']

# 站点名称
admin.site.site_header = '在线考试系统'

# 网页标题
admin.site.site_title = '在线考试系统后台'