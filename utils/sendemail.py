# encoding: utf-8
# @author: w4dll
# @file: sendemail.py
# @time: 2021/1/22 12:57


from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MaOnline0127.settings import EMAIL_FROM, HOST_IP

# 生成随机字符串
def random_str(random_length=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str

# 发送注册邮件
def send_register_eamil(email, send_type="register", host_ip=HOST_IP, code_count=4):

    # 生成随机的code放入链接
    code = random_str(code_count)

    # 保存注册码信息
    email_record = EmailVerifyRecord()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_record.save()

    # 定义邮件内容:
    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "用户注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://{1}:8000/active/{0}".format(code, host_ip)

    elif send_type == "forget":
        email_title = "用户找回密码链接"
        email_body = "请点击下面的链接找回你的账号: http://{1}:8000/reset/{0}".format(code, host_ip)

    elif send_type == "update_email":
        email_title = "修改邮箱验证码"
        email_body = "你的邮箱验证码为{0}".format(code)
    else:
        pass
        # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，发件人邮箱地址，收件人（是一个字符串列表）
    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

    # 如果发送成功
    if send_status:
        pass
