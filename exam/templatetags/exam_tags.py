# encoding: utf-8
# @author: w4dll
# @file: kingadmin_tags.py
# @time: 2021/2/19 18:29
from django.template import Library
from django.utils.safestring import mark_safe
import datetime
from utils.utils import dy
from exam.models import WrongRecord


register = Library()

# 自定义过滤器
@register.filter
def truncate_chars(value, show_nums=60):
    if value.__len__() > show_nums:
        return '{}.....'.format(value[0:show_nums])
    else:
        return value

@register.simple_tag
def render_paginator(querysets):
    ele = '<ul class="pagination">'

    # 首页
    if querysets.number > 1:
        p_ele = '<li><a href="?page=1">首页</a></li>'
    else:
        p_ele = '<li class="disabled"><a href="?page=1">首页</a></li>'
    ele += p_ele


    # 上一页
    if querysets.has_previous:
        if querysets.number > 1:
            p_ele = '<li><a href="?page={}"><<</a></li>'.format(querysets.number - 1)
        else:
            p_ele = '<li class="disabled"><a href="?page=1"><<</a></li>'
        ele += p_ele

    # 总页数,如果小于5，显示全部页码
    num_pages = querysets.paginator.num_pages
    page_range = querysets.paginator.page_range

    if num_pages < 6:
        for i in page_range:
            active = ''
            if querysets.number == i:
                active = 'active'
            ele += '<li class="{}"><a href="?page={}">{}</a></li>'.format(active, i, i)
    elif num_pages - querysets.number < 5:
        if querysets.number+2 > num_pages:
            for i in range(num_pages-4, num_pages+1):
                active = ''
                if querysets.number == i:
                    active = 'active'
                ele += '<li class="{}"><a href="?page={}">{}</a></li>'.format(active, i, i)
        else:
            for i in page_range:
                if abs(querysets.number - i) < 3:
                    active = ''
                    if querysets.number == i:
                        active = 'active'
                    ele += '<li class="{}"><a href="?page={}">{}</a></li>'.format(active, i, i)

    else:
        if querysets.number > 2:
            for i in page_range:
                if abs(querysets.number - i) < 3:
                    active = ''
                    if querysets.number == i:
                        active = 'active'
                    ele += '<li class="{}"><a href="?page={}">{}</a></li>'.format(active, i, i)
        else:
            for i in range(1, 6):
                active = ''
                if querysets.number == i:
                    active = 'active'
                ele += '<li class="{}"><a href="?page={}">{}</a></li>'.format(active, i, i)

    # 下一页
    if querysets.has_next:
        if querysets.number < querysets.paginator.num_pages:
            p_ele = '<li><a href="?page={}">>></a></li>'.format(querysets.number + 1)
        else:
            p_ele = '<li class="disabled"><a href="?page={}">>></a></li>'.format(querysets.paginator.num_pages)
        ele += p_ele

    # 末页
    if querysets.number < querysets.paginator.num_pages:
        p_ele = '<li><a href="?page={}">尾页</a></li>'.format(querysets.paginator.num_pages)
    else:
        p_ele = '<li class="disabled"><a href="?page={}">尾页</a></li>'.format(querysets.paginator.num_pages)
    ele += p_ele

    ele += '</ul>'
    return mark_safe(ele)

@register.simple_tag
def get_nums(querysets):
    return len(querysets)

# 根据试卷号和用户，筛选用户错题数量
@register.simple_tag
def get_wrong_nums(request, pid):
    objs = WrongRecord.objects.filter(user=request.user, paper__id=pid)
    return len(objs)

@register.simple_tag
def get_scores(querysets):
    scors = 0
    for item in querysets:
        scors += item.score
    return scors

@register.simple_tag
def render_num_choice(qs):
    eles = ''
    for i in range(1, len(qs)+1):
        eles += '<button>{}</button>'.format(i)
    return mark_safe(eles)

@register.simple_tag
def render_test_times(request, paper):
    if paper.chance_times == 0:
        return '999+'
    else:
        count1 = paper.record_set.filter(userid=request.user, is_valid=True).all().count()
        count = paper.chance_times - count1
        return count
