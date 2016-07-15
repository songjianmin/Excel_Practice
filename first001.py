#! -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 跟谁学邮箱配置
mailto_list = ["songjianmin@baijiahulian.com"]
mail_host = "121.52.212.26"  # 设置服务器
mail_port = 25
mail_user = "postmaster"  # 用户名
mail_pass = "bjhl123456"  # 口令
mail_postfix = "genshuixue.cn"  # 发件箱的后缀
mail_from = "baijaihulian"  # 来自

# 126邮件配置
mail_host_126 = "smtp.126.com"  # 设置服务器
mail_port_126 = 25
mail_user_126 = "liwf616"  # 用户名
mail_pass_126 = "bjhl@1234"  # 口令
mail_postfix_126 = "126.com"  # 发件箱的后缀
mail_from_126 = "baijaihulian"  # 来自

# 发送数据到跟谁学邮箱
def send_mail(to_list, subject="主题", content="内容"):  # to_list：收件人；sub：主题；content：邮件内容
    me = mail_from + "<" + mail_user + "@" + mail_postfix + ">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content, _subtype='html', _charset='utf8')  # 创建一个实例，这里设置为html格式邮件
    msg['Subject'] = Header(subject, charset="utf8")  # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        code, server_msg = s.connect(mail_host, port=mail_port)  # 连接smtp服务器
        print code, server_msg
        # s.login(mail_user, mail_pass)  #登陆服务器
        s.sendmail(me, [x + "@baijiahulian.com" for x in to_list], msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        import traceback

        traceback.print_exc()
        return False


# 发送数据到126邮箱
"""def send_mail_126(to_list, subject="主题", content="内容"):  # to_list：收件人；sub：主题；content：邮件内容
    me = mail_from_126 + "<" + mail_user_126 + "@" + mail_postfix_126 + ">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content, _subtype='html', _charset='utf8')  # 创建一个实例，这里设置为html格式邮件
    msg['Subject'] = Header(subject, charset="utf8")  # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        code, server_msg = s.connect(mail_host_126, port=mail_port_126)  # 连接smtp服务器
        print code, server_msg
        s.login(mail_user_126, mail_pass_126)  #登陆服务器
        s.sendmail(me, [x + "@126.com" for x in to_list], msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        import traceback

        traceback.print_exc()
        return False
"""
if __name__ == '__main__':
    if send_mail(mailto_list, subject="主题", content="内容"):
        print "发送成功"
    else:
        print "发送失败"