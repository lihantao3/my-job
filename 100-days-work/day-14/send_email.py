from email.mime.text import MIMEText
from smtplib import SMTP
from email.header import Header


def main():
    sender = 'tianjiaolilo@163.com'
    receiver = ['605405309@qq.com']
    message = MIMEText('用python发送邮件的示例代码', 'plain', 'utf-8')
    message['From'] = Header('tianjiao <tianjiaolilo@163.com>')
    message['To'] = Header('tianjiao', 'utf-8')
    message['Subject'] = Header('示例代码邮件', 'utf-8')
    smtper = SMTP('smtp.163.com')
    smtper.login(sender, 'KWVQAJMITWJZGQAL')
    smtper.sendmail(sender, receiver, message.as_string())
    print('邮件发送完成')


if __name__ == '__main__':
    main()
