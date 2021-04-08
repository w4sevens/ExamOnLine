"""exam0204_new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from exam import views

app_name = 'exam'

urlpatterns = [

    # 考试中心
    path('papers/info/', views.paper_info, name='paper_info'),

    # 试卷列表：展示、编辑、删除
    path('papers/list/', views.ListPaperView.as_view(), name='list_paper'),
    path('papers/<int:pid>/edit/', views.editpaper, name='editpaper'),
    path('papers/<int:pid>/delete/', views.deletepaper, name='deletepaper'),
    path('papers/<int:pid>/test/', views.test_paper, name='test_paper'),
    path('papers/<int:pid>/retest/', views.retest_paper, name='retest_paper'),
    path('papers/<int:pid>/save/word/', views.save_paper_word, name='save_paper_word'),

    # 所有试卷：展示、编辑、删除、显示所有成绩、导出EXCEL成绩
    path('papers/list/all/', views.list_all_paper, name='list_all_paper'),
    path('papers/result/<int:pid>/list/', views.result_of_paper, name='result_of_paper'),
    path('papers/result/<int:pid>/export/', views.export_result, name='export_result'),
    path('papers/<int:pid>/edit/all/', views.editpaperall, name='editpaperall'),
    path('papers/<int:pid>/delete/all/', views.deletepaperall, name='deletepaperall'),

    # 创建试卷：创建界面、刷新题目、保存试卷
    path('papers/create/', views.create_paper, name='create_paper'),  # 创建试卷
    path('papers/create/refresh_qb_count/', views.refresh_qb_count, name='refresh_qb_count'),  # 刷新题库数量
    path('papers/create/save/', views.save_paper, name='save_paper'),

    # 考试申请
    path('papers/proposal/list/', views.list_paper_proposal, name='list_paper_proposal'),
    path('papers/proposal/<int:pid>/agree/', views.paper_proposal_agree, name='paper_proposal_agree'),

    # 成绩列表:显示成绩、删除成绩
    path('results/list/', views.ListResultView.as_view(), name='list_result'),
    path('results/<int:rid>/delete/', views.delete_result, name='delete_result'),


    path('wrongs/list/', views.ListWrongsView.as_view(), name='list_wrongs'),

    # 题库操作
    path('qsbk/info/', views.qsbk_info, name='qsbk_info'),

    # 题库列表
    path('qsbk/list/', views.ListQSBKView.as_view(), name='list_questionbank_info'),
    path('qsbk/list/<int:qb_id>/detail/', views.QuestionBankDetailView.as_view(), name='questionbank_detail'),
    path('qsbk/list/<int:qb_id>/delete/', views.qsbk_delete, name='qsbk_delete'),
    path('qsbk/list/<int:qb_id>/edit/', views.qsbk_edit, name='qsbk_edit'),

    # 批量导入
    path('qsbk/import/', views.qsbk_import, name='qsbk_import'),
    path('qsbk/import/download/', views.qsbk_download, name='qsbk_download'),
    path('qsbk/import/show/', views.qsbk_show, name='qsbk_show'),   # 题库预览
    path('qsbk/import/save/', views.qsbk_save, name='qsbk_save'),

    # 训练中心
    path('train/info/', views.train_info, name='train_info'),

    # 我要训练
    path('train/list/', views.train_list, name='train_list'),
    path('train/<int:qid>/random_test/', views.random_test, name='random_test'),
    path('train/<int:qid>/sequence/', views.train_sequence, name='train_sequence'),
    path('train/<int:qid>/check/', views.train_check, name='train_check'),
    path('train/submit/', views.train_submit, name='train_submit'),

    # 训练记录：训练记录列表、查看错题、删除记录
    path('train/record/', views.train_record, name='train_record'),
    path('train/delete_record/<int:wid>/', views.delete_record, name='delete_record'),
    path('train/listwrong/<int:wid>/', views.listwrong, name='listwrong'),

    # 所有记录
    path('train/allrecord/', views.train_allrecord, name='train_allrecord'),

    # 问卷调查 questionnaire
    path('questionnaire/info/', views.questionnaire_info, name='questionnaire_info'),

]
