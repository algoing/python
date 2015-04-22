#!/usr/bin/python
#-*- coding: utf-8 -*-

import smtplib
import getpass
from email.mime.text import MIMEText

mailto_list=['1447704948@qq.com','zijian1012@163.com']
mail_host = "smtp.163.com"
mail_user = "zijian1012"
mail_pass=getpass.getpass("Input the passwd:")
mail_subject="hello"
mail_postfix="163.com"
file = "/etc/passwd"

f = open(file,'r')
messages = f.readlines()
f.close()
messages = "".join(messages)

def send_mail(to_list,sub,content):
    me = "hello" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content,_subtype="mixed",_charset="utf-8")
    msg['Subject'] = sub
    msg['From'] = me
    msg['to'] = ";".join(to_list)

    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    if send_mail(mailto_list,mail_subject,messages):
        print "send ok"
    else:
        print "send error"
