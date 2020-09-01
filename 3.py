from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

# 邮箱smtp服务器
host_server = 'smtp.163.com'

# pwd为邮箱的授权码
pwd = '**'

# 发件人的邮箱
sender = '**@163.com'

# 收件人邮箱
# receiver = '**@qq.com'
receiver = input('请输入收件人的邮箱：')

# 邮件标题
mail_title = input('请输入邮件标题：')

# 邮件的正文内容
mail_content = input('请输入邮件正文：')

# ssl登录
smtp = SMTP_SSL(host_server)

# set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(0)

smtp.ehlo(host_server)

smtp.login(sender, pwd)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender
msg["To"] = receiver
cc = smtp.sendmail(sender, receiver, msg.as_string())
if cc == {}:
    print('发送成功！')
else:
    print(cc)
smtp.quit()
