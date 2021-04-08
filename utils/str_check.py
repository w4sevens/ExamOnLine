# encoding: utf-8
# @author: w4dll
# @file: str_check.py
# @time: 2021/3/5 12:33

checkstr='abcdefghijklmnopqrstuvwxayABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

# 验证用户名是否为字母和数字的组合，否则不合法
def is_login_name(str1, lenght=3):
    if not isinstance(str1, str):
        print('用户名只能是字母和数字的组合！')
        return False

    # print([s in checkstr for s in str1])
    if all([s in checkstr for s in str1]):
        return True
    else:
        print('用户名不合法，必须是数字或者字母！')
        return False

if __name__ == '__main__':
    print(is_login_name('-123'))