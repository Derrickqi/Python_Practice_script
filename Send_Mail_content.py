import smtplib
from email.mime.text import MIMEText

subject = "邮件主题"  # 邮件的主题
content = "system errorr,please check"  # 邮件内容
sender = "xxxx@163.com"  # 发件人
password = 'passwd'  # 刚才我们在163邮箱里设置的授权密码
receivers = ["xxxxx@qq.com"]  # 收件人
for receiver in receivers:
    message = MIMEText(content, "html", "utf-8")
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject

    smtp = smtplib.SMTP_SSL('smtp.163.com', 994)
    smtp.login(sender, password)
    smtp.sendmail(sender, [receiver], message.as_string())
    smtp.close()
