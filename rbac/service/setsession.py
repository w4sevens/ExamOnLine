# encoding: utf-8
# @author: w4dll
# @file: setsession.py
# @time: 2021/2/28 11:03
# from users.models import Role
from rbac.models import Role
from utils.utils import dy

def initial_session(user_obj, request):
    """
    将当前登录人的所有权限列表和所有菜单权限列表注入session
    :param user_obj: 当前登录用户对象
    :param request: 请求对象HttpRequest
    """
    # 查询当前登录人的所有权限列表
    # todo 注意这里定义的是userprofile，后台共用的密码，最好不要这么定义在一起，尽量松耦合，Role最好定义在rbac内部
    ret = Role.objects.filter(userprofile=user_obj).values('permissions__url',
                                                           'permissions__is_menu',
                                                           'permissions__is_menu__icon',
                                                           'permissions__is_menu__title',
                                                           'permissions__is_menu__sequence',
                                                           'permissions__is_menu__layer',
                                                           ).distinct()
    permission_list = []
    menu_list = []

    # dy('初始化当前用户的权限')

    for item in ret:
        # 存入权限
        permission_list.append(item['permissions__url'])

        # 如果菜单存在，存入菜单对象
        # menu = Menus.objects.filter(pk=item['permissions__is_menu']).first()
        if item['permissions__is_menu']:
            menu_list.append({'title': item['permissions__is_menu__title'],
                              'icon': item['permissions__is_menu__icon'],
                              'sequence': item['permissions__is_menu__sequence'],
                              'layer': item['permissions__is_menu__layer'],
                              'url': item['permissions__url'],
                              })

    # 菜单进行排序
    menuLenght = len(menu_list)
    for i in range(menuLenght):
        m = menu_list[i]
        for j in range(i+1, menuLenght):
            if m['sequence'] > menu_list[j]['sequence']:
                menu_list[i] = menu_list[j]
                menu_list[j] = m
                m = menu_list[i]
    # dy(menu_list)

    # todo 这里只做到二级菜单，不继续深入
    menu_list1 = []
    dy(menu_list)
    for menu in menu_list:
        if menu['layer'] == 0:
            # dy(menu.permission_set())
            menu_list1.append({'url': menu['url'],
                               'title': menu['title'],
                               'icon': menu['icon'],
                               'children': []})
        elif menu['layer'] == 1:
            menu_list1[-1]['children'].append({'url': menu['url'],
                                               'title': menu['title'],
                                               'icon': menu['icon']})
        else:
            pass
    # dy(menu_list1)
    # dy('权限列表', permission_list)

    request.session['permission_list'] = permission_list
    request.session['menu_list'] = menu_list1
    dy('权限列表', permission_list)