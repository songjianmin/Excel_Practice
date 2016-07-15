#! usr/bin/env python
#! -*- coding:utf8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host_baihulian = "172.24.45.7"
mail_port_baijiahulian = 25
mail_user_baijiahulian = "songjianmin"
mail_pwd_baijiahulian = "sjm0217@"
mail_postfix_baijiahulian = "baijiahulian.com"
mail_from_baijiahulian = "baijiahulian"

#163 邮箱设置
mailto_list = ["songjianmin@baijiahulian.com"]
mail_host_163 = "smtp.163.com" #设置163邮箱发件服务器
mail_port = 25
mail_user_163 = "songjianmin_job" #用户名
mail_pwd_163 = "sjm814630" #口令
mail_postfix_163 = "163.com" #发件箱后缀
mail_from_163 = "genshuixue" #来自`

#发送邮件

def send_mail_baijiahulian(to_list,subject,content):
    me = mail_from_baijiahulian + "<"+mail_user_baijiahulian + "@" + mail_postfix_baijiahulian + ">"
    msg = MIMEText(content,_subtype='plain',_charset='utf8')
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        sm = smtplib.SMTP()
        code,sm_msg = sm.connect(host=mail_host_baihulian,port=mail_port_baijiahulian)
        print code,sm_msg
        sm.login(mail_user_baijiahulian,mail_pwd_baijiahulian)
        sm.sendmail(me,mailto_list,msg.as_string())
        sm.close()
        return True
    except Exception,e:
        print e
        import traceback
        traceback.print_exc()
        return False


def send_mail_163(to_list,subject = "主题",content = "内容"):   #to_list:收件人；subject：主题；content：邮件内容
    me = mail_from_163 + "<" +mail_user_163 + "@" + mail_postfix_163 + ">"
    msg = MIMEText(content,_subtype='plain',_charset='utf8')
    #msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = ":" .join(to_list)
    try:
        s = smtplib.SMTP()
        code,server_msg = s.connect(mail_host_163,mail_port)
        print code,server_msg
        s.login(mail_user_163,mail_pwd_163)
        s.sendmail(msg['From'],msg['To'],msg.as_string())
        s.close()
        return True
    except Exception:
        import traceback
        traceback.print_exc()
        return False
if __name__ == '__main__':
    if send_mail_baijiahulian(mailto_list,subject="Python 测试",content="上午好！"):
        print "发送成功"
    else:
        print "发送失败"
    if send_mail_163(mailto_list,subject = "Python 测试",content = "上午好！"):
        print "发送成功"
    else:
        print "发送失败"