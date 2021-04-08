from django.db import models
from users.models import UserProfile
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import Units

class ProposalRecord(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='申请人', on_delete=models.CASCADE)
    paper = models.ForeignKey('TestPaper', verbose_name='试卷',  on_delete=models.CASCADE)
    time = models.DateTimeField('申请时间', auto_now_add=datetime.now)
    is_handled = models.BooleanField('处理', default=False)

    class Meta:
        verbose_name = '考试申请记录'
        verbose_name_plural = verbose_name


# 试卷表
class TestPaper(models.Model):
    paper_name = models.CharField('试卷名称', max_length=40)
    test_time = models.IntegerField('考试时长', help_text='单位是分钟')
    add_time = models.DateTimeField('添加时间', auto_now_add=datetime.now)
    create_person = models.ForeignKey(UserProfile, verbose_name="出题人", on_delete=models.SET_NULL, null=True)
    applyto = models.ManyToManyField(Units, verbose_name='适用人员', blank=True, null=True)
    include_qinfo = models.ManyToManyField('QuestionInfo', verbose_name='包含题库', blank=True, null=True, default='')

    # 考试机会次数,0表示不限次数
    chance_times = models.IntegerField('可考次数', default=0)

    # 热度，试卷被考次数
    hot_nums = models.IntegerField('热度', default=0)

    # 随机模式
    random_type = ((0, '固定出题'), (1, '随机出题'))
    is_random = models.IntegerField('是否随机', choices=random_type, default=0)

    # 试卷各型题目数量
    singel_count = models.IntegerField('单选数量', default=0)
    multi_count = models.IntegerField('多选数量', default=0)
    judge_count = models.IntegerField('判断数量', default=0)
    fillin_count = models.IntegerField('填空数量', default=0)
    ans_count = models.IntegerField('问答数量', default=0)


    class Meta:
        # 选择这个表之后显示的名字
        verbose_name = '试卷'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.paper_name

    def get_singles(self):
        return self.questionbank_set.filter(question_type='single').all()

    def get_single_count(self):
        if self.is_random:
            return self.singel_count
        else:
            return len(self.get_singles())

    def get_single_scores(self):
        sum1 = sum([que.score for que in self.get_singles()])
        return sum1

    def get_multiples(self):
        return self.questionbank_set.filter(question_type='multi').all()

    def get_multiple_count(self):
        if self.is_random:
            return self.multi_count
        else:
            return len(self.get_multiples())

    def get_multiple_scores(self):
        sum1 = sum([que.score for que in self.get_multiples()])
        return sum1

    def get_judges(self):
        return self.questionbank_set.filter(question_type='judge').all()

    def get_judge_count(self):
        if self.is_random:
            return self.judge_count
        else:
            return len(self.get_judges())

    def get_judge_scores(self):
        sum1 = sum([que.score for que in self.get_judges()])
        return sum1

    def get_counts(self):
        return self.get_single_count()+self.get_judge_count()+self.get_multiple_count()

    def get_scores(self):
        if self.is_random:
            return None
        else:
            return self.get_single_scores()+self.get_judge_scores()+self.get_multiple_scores()

# 题库信息
class QuestionInfo(models.Model):
    name = models.CharField('题库名称', max_length=128)
    create_person = models.ForeignKey(UserProfile, verbose_name='创建人', on_delete=models.CASCADE)
    add_time = models.DateTimeField('导入时间', auto_now_add=True)
    applyto = models.ManyToManyField(Units, verbose_name='适用人员', blank=True, null=True, default='')
    class Meta:
        verbose_name = '题库信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 题库表
class QuestionBank(models.Model):

    title = models.TextField('题干')
    question_bank_name = models.ForeignKey(QuestionInfo, null=True, blank=True, on_delete=models.CASCADE)

    type_choice = ((0, '单选题'), (1, '多选题'), (2, '判断题'), (3, '填空题'), (4, '问答题'))
    question_type = models.IntegerField('题目类型', choices=type_choice)
    pid = models.ManyToManyField(TestPaper, verbose_name='所属试卷', null=True, blank=True)
    answer = models.TextField('答案')

    diff_choice = ((0, '简单'), (1, '中等'), (2, '难'))
    difficulty = models.IntegerField('难度', choices=diff_choice)
    score = models.IntegerField('分值', default=1)

    class Meta:
        verbose_name = '题库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# 成绩表
class Record(models.Model):
    userid = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    papername = models.ForeignKey(TestPaper, on_delete=models.CASCADE, verbose_name='考试科目')
    grade = models.FloatField('成绩')
    test_time = models.DateTimeField(verbose_name='考试时间', auto_now_add=datetime.now)

    # 成绩是否有效，设置考试次数时，申请补考，原考试记录变为无效
    is_valid = models.BooleanField('是否有效', default=True)

    class Meta:
        verbose_name = '考试记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s:%s>' % (self.userid, self.grade)

from utils.utils import dy
class WrongRecord(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE, verbose_name='试卷')
    question = models.ForeignKey(QuestionBank, on_delete=models.CASCADE, verbose_name='题目')
    error_times = models.IntegerField('错误次数', default=0)
    my_ans = models.TextField('我的答案', default='')

    class Meta:
        verbose_name = '错题集'
        verbose_name_plural = verbose_name


class TrainRecord(models.Model):
    # todo 合理设计训练记录题库
    title = models.CharField(verbose_name='训练科目', max_length=128, default='')
    train_type = models.CharField('训练内容', max_length=256)
    time = models.DateTimeField('结束时间', auto_now_add=True)
    starttime = models.DateTimeField('开始时间', default='2000-01-01 00:00:00', blank=True, null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='姓名')
    wrong = models.ManyToManyField(QuestionBank, verbose_name='错题')


    class Meta:
        verbose_name = '训练记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_time_diff(self):
        '''
        全部训练时间
        :return: 返回秒
        '''
        timediff = self.time - self.starttime
        return timediff.total_seconds()

    def get_time_of_this_year(self):
        """
        今年以来的训练时间，如果结束时间在今年则算入今年
        :return: 返回秒
        """
        # dy(self.time.tzinfo, datetime.now().tzinfo)
        if self.starttime.year == datetime.now().year:
            timediff = self.time - self.starttime
            return timediff.total_seconds()
        else:
            return 0









