"""
if分支判断用户名和密码是否正确
"""

username = input('请输入用户名： ')
password = input('请输入密码： ')
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')
