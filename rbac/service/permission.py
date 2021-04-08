# encoding: utf-8
# @author: w4dll
# @file: permission.py
# @time: 2021/2/28 10:18
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, HttpResponse, render
import re
from django.conf import settings
from utils.utils import dy

class PermissionMiddleWare(MiddlewareMixin):
    def process_request(self, request):

        # 设置白名单放行,将白名单放在setting文件中，
        for reg in settings.WHITE_LIST:
            ret = re.search(reg, request.path)
            if ret:
                # dy('登录或者后台放行')
                return None

        # 检验是否登录
        if not request.user.is_authenticated:
            # dy('用户未登录，请先登录')
            return redirect(settings.LOGIN_URL)

        # 检验权限,如果没有权限403
        permission_list = request.session.get('permission_list')
        if not permission_list:
            return render(request, 'rbac/page_403.html')

        # dy('下面进行权限验证', request.path)
        for reg in permission_list:
            reg = '^{}$'.format(reg)
            ret = re.search(reg, request.path)
            # dy(reg, ret)

            if ret:
                # dy('权限比对成功', ret, reg)
                return None
        # dy('权限验证失败，无操作权限！')
        return render(request, 'rbac/page_403.html')