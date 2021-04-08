# encoding: utf-8
# @author: w4dll
# @file: pagenator.py
# @time: 2021/2/28 14:11

from pure_pagination import Paginator, PageNotAnInteger


def get_pagenator(request, objs, num=10):
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(objs, num, request=request)  # 每页显示2个元素
    res = p.page(page)
    return res