"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

import re


def main():
    username = input('请输入您的用户名：')
    while not (re.match(r'^\w+$', username) and 6 <= len(username) <= 20):
        username = input('请输入有效的用户名：')
    qq = input('请输入您的qq号码：')
    while not re.match(r'^[1-9]\d{4,11}$', qq):
        qq = input('请输入正确的qq号：')
    print('您的用户名为：%s\n您的qq号码为：%s' % (username, qq))


if __name__ == '__main__':
    main()
