#!urs/bin/python
#! -*- coding:utf8 -*-
"""
import glob,sys
"""
"""
import glob
from number import Number
print (glob.glob('person*'))
print ('\n************\n')
X = Number(5)
Y = X - 2
print (Y.data)
"""

"""
import Spam
a = Spam.Spam()
b = Spam.Spam()
c = Spam.Spam()
a.print NumInstances()
Spam.Spam.printNumInstances(a)
"""
"""
import classtools
reload(classtools)
x = classtools.Adder()
x.add(1,2)

x = classtools.ListAdder()
x.add([1],[2])
"""

'''
发送txt文本邮件
小五义：http://www.cnblogs.com/xiaowuyi
'''
import smtplib
from email.mime.text import MIMEText
mailto_list=["317804344@qq.com"]
mail_host="220.181.12.208"  #设置服务器
mail_user="songjianmin_job"    #用户名
mail_pass="sjm123@"   #口令
mail_postfix="163.com"  #发件箱的后缀

def send_mail(to_list,sub,content):
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        import traceback
        traceback.print_exc()
        return False
if __name__ == '__main__':
    if send_mail(mailto_list,"hello","hello world！"):
        print "发送成功"
    else:
        print "发送失败"