
'''
发送附件邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sys import argv
from email.mime.application import MIMEApplication

mailto_list=[]
# 源邮箱
mail_host="smtp.163.com:25"  #设置服务器
mail_user="user"     #发件用户名(换成自己的)
mail_pass="passwd"   #口令（换成自己的）
debug_level=0       #是否开启debug

def send_mail(to_list,sub,content):
    me=mail_user
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    #发送的文件
    xlsx = MIMEApplication(open('worker.xlsx', 'rb').read())
    xlsx["Content-Type"] = 'application/octet-stream'
    xlsx.add_header('Content-Disposition', 'attachment', filename='worker.xlsx')
    msg.attach(xlsx)
    try:
        server = smtplib.SMTP()
        server.set_debuglevel(debug_level)
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False
if __name__ == '__main__':
    try:
# 目标邮箱
        mailto_list='389994262@qq.com'
        sub='389994262@qq.com'
        content='<h1>测试，能用告诉我<h1>'
    except:
        print ("python send_mail.py 'user1@xx.com;user2@xx.com' sub content")
        exit()

    if send_mail(mailto_list,sub,content):
        print ("发送成功")
    else:
        print ("发送失败")

