# encoding: utf-8
# @author: w4dll
# @file: testview.py
# @time: 2021/2/8 22:07
from django.shortcuts import render, HttpResponse, redirect

from django.views import View

class TestView(View):
    def get(self, request):
        return render(request, 'indexbase.html')
