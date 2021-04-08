# encoding: utf-8
# @author: w4dll
# @file: shuffle.py
# @time: 2021/3/11 18:44
import random


# 抽牌算法，从一组排lst中随机抽取count张
def shuffle(lst, count):
    ln = len(lst)
    if ln <= count:
        return lst
    else:
        i = 0
        while i < ln:
            t = lst[i]
            j = random.randint(0, ln - 1)
            lst[i] = lst[j]
            lst[j] = t
            i += 1
        return lst[:count]


# 洗牌算法，将lst随机重新排列
def shuffle1(lst):
    ln = len(lst)
    if ln <= 1:
        return lst

    i = 0
    while ln > 1:
        j = int(random.random() * ln)
        t = lst[i]
        lst[i] = lst[i + j]
        lst[i + j] = t
        i = i + 1
        ln = ln - 1

    return lst
