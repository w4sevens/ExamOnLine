# encoding: utf-8
# @author: w4dll
# @file: utils.py
# @time: 2021/1/22 18:53
from pure_pagination import Paginator, PageNotAnInteger
def get_pagenator(request, objs, num=10):
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(objs, num, request=request)

    try:
        res = p.page(page)
    except:
        res = p.page(1)
    return res


def dy(val, *args):
    print('-------------------------------->>>', val)
    for i in args:
        print('-------------------------------->>>', i)