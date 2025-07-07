import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


def send_email():
    # 发件人和收件人信息
    print("开始发送报错邮件")
    sender_email = 'young_owl@qq.com'  # 我的QQ邮箱
    receivers = ['youngowlgi@outlook.com']  # 接收邮件的邮箱（还是我的QQ邮箱）

    # 邮件内容
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')

    # 设置发件人信息，格式为 "显示名称 <邮箱地址>"
    message['From'] = formataddr((str(Header("发件人名称", 'utf-8')), sender_email))
    message['To'] = Header("收件人名称", 'utf-8')
    message['Subject'] = Header("程序出现报错", 'utf-8')

    # SMTP服务器配置
    smtp_server = 'smtp.qq.com'  # QQ邮箱的SMTP服务器
    smtp_port = 587  # TLS端口
    username = sender_email  # 你的QQ邮箱地址
    password = 'keeyhkfscvaccjcg'  # 你的QQ邮箱授权码，不是登录密码

    try:
        # 创建SMTP对象并连接服务器
        smtpObj = smtplib.SMTP(smtp_server, smtp_port)
        smtpObj.starttls()  # 启用TLS加密

        # 登录SMTP服务器
        smtpObj.login(username, password)

        # 发送邮件
        smtpObj.sendmail(sender_email, receivers, message.as_string())
        print("报错邮件发送成功")

    except smtplib.SMTPException as e:
        print(f"Error: 无法发送邮件 - {e}")
    finally:
        # 关闭连接
        if 'smtpObj' in locals():
            smtpObj.quit()