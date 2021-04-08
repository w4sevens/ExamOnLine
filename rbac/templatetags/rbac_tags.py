# encoding: utf-8
# @author: w4dll
# @file: rbac_tags.py
# @time: 2021/2/28 14:09
from django.template import Library
from django.utils.safestring import mark_safe
from utils.utils import dy
from users.models import Units

register = Library()


@register.simple_tag
def render_sidebar(request):
    # dy('渲染菜单')
    menu_list = request.session.get('menu_list')
    if not menu_list:
        return ''

    # 构造标签
    elmt = ''
    for menu in menu_list:
        # 给当前一级标题标签上色
        if request.path == menu['url']:
            elmt += '<li class="mydropdown"><div ><a href="{}" style="color:#57eaea"><span class="{}"></span>{}</a></div>' \
                .format(menu['url'], menu['icon'], menu['title'])
        else:
            elmt += '<li class="mydropdown"><div><a href="{}"><span class="{}"></span>{}</a></div>'\
                .format(menu['url'], menu['icon'], menu['title'])
        if menu['children']:
            # 如果是当前路径，展开标签，否则关闭标签
            if request.path in [cc['url'] for cc in menu['children']] or request.path == menu['url']:
                elmt += '<ul class="dropdown-menu1" style="display:block">'
            else:
                elmt += '<ul class="dropdown-menu1 hide">'

            for c1 in menu['children']:
                # 给二级标题上色
                if request.path == c1['url']:
                    elmt += '<li><a href="{}" style="color:#57eaea"><span class="{}"></span> {}</a></li>'.format(
                        c1['url'], c1['icon'], c1['title'])
                else:
                    elmt += '<li><a href="{}"><span class="{}"></span> {}</a></li>'.format(
                        c1['url'], c1['icon'], c1['title'])
                if request.path == c1['url']:
                    elmt.replace('hide', '')
            elmt += '</ul>'
    elmt += '</li>'
    return mark_safe(elmt)


@register.simple_tag
def render_train_time(times):
    a = int(times/60)
    if a == 0:
        return str(times) + '秒'
    b = int(times/3600)
    if b == 0:
        return str(a) + '分' + str(times-60*a) + '秒'
    else:
        return str(b) +'时'+ str(int((times-3600*b)/60)) + '分'

@register.simple_tag
def get_unit_from_name(uname):
    units = Units.objects.filter(unit_name=uname)
    for u in units:
        if u.logo2:
            dy(u.logo2.logo)
            return u.logo2.logo
    return None