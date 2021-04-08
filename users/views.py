from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.utils.safestring import mark_safe

import datetime

from utils.utils import dy
from utils.utils import get_pagenator
from utils.str_check import is_login_name

from users.userforms import UserModelForm, UserProfileModelForm
from users import models
from users.models import UserProfile, Units

from rbac.service.setsession import initial_session
from rbac.models import Role

from exam.models import Record, TrainRecord, TestPaper


# 首页
class IndexView(View):
    def get(self, request):
        rcds = Record.objects.filter(is_valid=True).all()

        # 单位成绩展示
        uscore_dict = {}
        for rd in rcds:
            unit = rd.userid.unit.unit_name
            if unit in uscore_dict:
                uscore_dict[unit].append(rd.grade)
            else:
                uscore_dict[unit] = [rd.grade]
        for u, vlist in uscore_dict.items():
            uscore_dict[u] = round((sum(vlist)/len(vlist)), 2)
        uscore_list = sortDict(uscore_dict)[:3]  # 显示前3名
        # dy(uscore_list)

        #1 综合成绩排行，取所有成绩平均
        score_dict = {}
        for r in rcds:
            user = r.userid
            if user in score_dict:
                score_dict[user].append(r.grade)
            else:
                score_dict[user] = [r.grade]
        # 平均
        for u, v in score_dict.items():
            score_dict[u] = round(sum(v) / len(v), 2)
        ls_socres = sortDict(score_dict)


        #2 成绩排行，取最近一次发布的考试成绩排行
        paper = TestPaper.objects.all().order_by('-add_time').first()
        scores = Record.objects.filter(papername=paper).all().order_by('-grade')

        #3 一周训练时间榜
        dt = datetime.datetime.now() - datetime.timedelta(days=7)
        trcds = TrainRecord.objects.filter(starttime__gt=dt).all()

        # 所有人近一周训练时间字典
        train_dict = {}
        for tr in trcds:
            if tr.user in train_dict:
                train_dict[tr.user] += int(tr.get_time_diff())
            else:
                train_dict[tr.user] = int(tr.get_time_diff())

        # 排序
        trainList = sortDict(train_dict)
        return render(request, 'exam/index.html', locals())

def sortDict(dic):
    ls = list(dic.items())
    lenght = len(ls)
    for i in range(lenght):
        for j in range(i+1, lenght):
            if ls[i][1] < ls[j][1]:
                tmp = ls[i]
                ls[i] = ls[j]
                ls[j] = tmp
    return ls

class LoginView(View):
    def post(self, request):
        dy('提交登录信息')

        # 获取表单信息
        uname = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=uname, password=password)
        if user:
            login(request, user)
            dy('用户登录成功, 注入权限到session中')
            initial_session(user, request)
            return redirect('index')
        else:
            dy('用户登录失败！')
            error_msg = '用户名或密码错误！'
            return render(request, 'exam/login.html', locals())

    def get(self, request):
        return render(request, 'exam/login.html')


class RegisterView(View):
    def get(self, request):
        units = models.Units.objects.all()
        return render(request, 'exam/register.html', locals())

    def post(self, request):
        username = request.POST.get('username')
        nick_name = request.POST.get('nick_name')
        idcard = request.POST.get('idcard')
        gender = request.POST.get('gender')
        unit = request.POST.get('unit')
        password = request.POST.get('password')

        units = models.Units.objects.all()

        # 是否注册过
        id = models.UserProfile.objects.filter(idcard=idcard).first()
        if id:
            error = mark_safe('您已注册，如忘记密码，可申请<a href="/register/forgort_pwd/{}/">找回账号</a>。'.format(idcard))
            reback = 'reback'
            return render(request, 'exam/register.html', locals())

        # 用户名是否已存在
        users = models.UserProfile.objects.filter(username=username).first()
        if users:
            error = '当前用户名【{}】已存在！'.format(username)
            return render(request, 'exam/register.html', locals())

        # 注册用户
        u = models.Units.objects.get(pk=unit)
        regist_user = models.UserProfile.objects.create(
            username=username, password=make_password(password),
            nick_name=nick_name, gender=gender, idcard=idcard,
            unit=u)
        role = Role.objects.filter(name='一般用户').first()
        regist_user.role.add(role)
        # todo 这里要保存吗？
        a = '<a href="/login/">登录</a>'
        return HttpResponse(mark_safe('注册成功，请' + a))


def forgort_pwd(request, idcard):
    if request.method == 'GET':
        return render(request, 'exam/forgort_pwd.html', locals())
    else:
        username = request.POST.get('username')
        nick_name = request.POST.get('nick_name')
        password = request.POST.get('password')

        user = models.UserProfile.objects.filter(username=username, nick_name=nick_name,
                                                 idcard=idcard).first()
        if not user:
            error = '没有找到符合当前用户名和姓名的用户！'
        else:
            user.set_password(password)
            error = mark_safe('重置密码成功！<a href="/login/">登录</a>')
        return render(request, 'exam/forgort_pwd.html', locals())


class LogoutView(View):
    def get(self, request):
        logout(request)
        # dy('退出登录,清空session')
        return redirect('login')


# 用户管理首页，显示所有用户的概要信息
def userinfo(request):
    users_all = UserProfile.objects.all().count()
    units = Units.objects.all()
    userdict = {}
    for u in units:
        count1 = u.userprofile_set.all().count()
        if u.unit_name in userdict:
            userdict[u.unit_name] += count1
        else:
            userdict[u.unit_name] = count1
    unit_name_count = len(userdict)
    return render(request, 'user_info.html', locals())


# 显示二级单位人员信息
def user_unit_detail(request, ustr):
    dy('进入user_unit_detail')
    unit2 = models.Units.objects.filter(unit_name=ustr).all()
    count_all = 0
    for u in unit2:
        count_all += u.userprofile_set.count()
    return render(request, 'user_info_detail.html', locals())


# 展示所有用户信息
def userlist(request):
    users1 = UserProfile.objects.all().order_by('unit')
    users = get_pagenator(request, users1)
    return render(request, 'user_list.html', locals())


# 编辑用户
def useredit(request, uid):
    user_obj = UserProfile.objects.get(pk=uid)
    if request.method == 'GET':
        form_obj = UserModelForm(instance=user_obj)
        return render(request, 'user_edit.html', {'form_obj': form_obj})
    else:
        form_obj = UserModelForm(request.POST, instance=user_obj)
        if form_obj.is_valid():
            form_obj.save()     # 由于图片存在FILES中，用POST无法保存

            # 保存图片
            file = request.FILES.get('image')
            user_obj.image = file
            user_obj.save()

            page = request.GET.get('page', 1)
            return redirect('/user/list/?page={}'.format(page))
        else:
            return render(request, 'user_edit.html', {'form_obj': form_obj})


# 删除用户功能
def userdelete(request, uid):
    UserProfile.objects.get(pk=uid).delete()
    page = request.GET.get('page', 1)
    return redirect('/user/list/?page={}'.format(page))


# 添加用户
def useradd(request):
    if request.method == "GET":
        form_obj = UserProfileModelForm()
        return render(request, 'user_add.html', locals())
    else:
        # dy('用户提交保存', request.POST)
        user_dict = {}
        for item in request.POST:
            if item != 'csrfmiddlewaretoken':
                if item == 'password':
                    user_dict[item] = make_password(request.POST.get(item, ''))
                elif item == 'unit':
                    user_dict[item] = Units.objects.get(pk=request.POST.get(item, ''))
                else:
                    user_dict[item] = request.POST.get(item, '')
        user_dict['date_joined'] = datetime.datetime.now()
        try:
            UserProfile.objects.create(**user_dict)
            return redirect('user:userlist')
        except:
            a = mark_safe('添加失败。<a href="javascript:history.back()">返回</a>')
            return HttpResponse(a)


# 个人中心，概要信息
def showme(request):
    user = request.user
    units = Units.objects.all().order_by('unit_name')
    return render(request, 'show_me.html', locals())


# 用户修改头像
def img_upload(request):
    # dy(request, request.POST, request.FILES)
    if request.method == 'POST':
        file = request.FILES.get('filename')
        request.user.image = file
        request.user.save()
        return HttpResponse('success')
    return HttpResponse('fail')


# 保存用户信息
def usersave(request):
    user = request.user
    try:
        user.nick_name = request.POST.get('name', '')
        user.birthday = request.POST.get('birthday', '')
        user.gender = request.POST.get('gender', '')
        user.address = request.POST.get('address', '')
        user.mobile = request.POST.get('mobile', '')
        unit = request.POST.get('unit', '')
        uobj = Units.objects.get(pk=unit)
        user.unit = uobj
        user.save()
        a = mark_safe('保存成功！<a href="javascript:history.back()">返回。</a>')
    except:
        a = mark_safe('保存失败，请检查输入日期是否正确！<a href="javascript:history.back()">返回。</a>')
    return HttpResponse(a)


# 修改密码
def change_pwd(request):
    if request.method == 'GET':
        return render(request, 'change_pwd.html')
    else:
        # todo 密码修改后，3秒后跳转重新登录！
        dy(request.POST)
        oldpwd = request.POST.get('oldpwd', '')
        newpwd = request.POST.get('pwd1', '')
        if not is_login_name(newpwd):
            return render(request, 'change_pwd.html', {'error': '密码不合法，请输入数字、字母、下划线的组合！'})

        user = authenticate(username=request.user.username, password=oldpwd)
        if not user:
            return render(request, 'change_pwd.html', {'error': '原始密码错误！'})
        else:
            user.set_password(newpwd)
            user.save()

            # 重新登录
            return redirect('login')


# 编辑自己
def edit_myself(request):
    form_obj = UserProfileModelForm(instance=request.user)
    return render(request, 'edit_myself.html', locals())


# 设置信息
def config(request):
    return render(request, 'config_info.html')


# 单位信息列表
def unitlist(request):
    units = Units.objects.all().order_by('unit_name')
    return render(request, 'config_unit_list.html', locals())


# 添加单位
def unitadd(request):
    if request.method == 'GET':
        return render(request, 'config_unit_add.html', locals())
    else:
        fname = request.POST.get('unit_full_name')
        unit_name = request.POST.get('unit_name')
        uname2 = request.POST.get('uname2')

        try:
            Units.objects.create(unit_name=unit_name, unit_full_name=fname, uname2=uname2)
            return redirect('user:unitlist')
        except:
            error = '当前单位已存在！'
            return render(request, 'config_unit_add.html', locals())


# 编辑单位信息
def edit_unit(request, uid):
    units = models.Units.objects.get(pk=uid)
    if request.method == 'GET':
        fname = units.unit_full_name
        unit_name = units.unit_name
        uname2 = units.uname2
        logos = models.Logo.objects.all()
        return render(request, 'config_unit_add.html', locals())
    else:
        units.fname = request.POST.get('unit_full_name')
        units.unit_name = request.POST.get('unit_name')
        units.uname2 = request.POST.get('uname2')
        l1 = request.POST.get('logo1')
        if l1:
            units.logo1 = models.Logo.objects.get(pk=l1)
        l2 = request.POST.get('logo2')
        if l2:
            units.logo2 = models.Logo.objects.get(pk=l2)
        l3 = request.POST.get('logo3')
        if l3:
            units.logo3 = models.Logo.objects.get(pk=l3)

        try:
            units.save()
            return redirect('user:unitlist')
        except:
            error = '当前单位已存在！'
            return render(request, 'config_unit_add.html', locals())


# 删除单位信息
def delete_unit(request, uid):
    models.Units.objects.get(pk=uid).delete()
    return redirect('user:unitlist')
