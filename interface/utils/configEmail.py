import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from interface.utils.getHtmlPath import get_htmlPath



# 发送邮件方法
class SendEmail(object):
    def __init__(self, username, passwd, recv, title, content,
                 file=None, ssl=False,
                 email_host='smtp.163.com', port=25, ssl_port=465):
        self.username = username
        self.passwd = passwd
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
        self.email_host = email_host
        self.port = port
        self.ssl = ssl
        self.ssl_port = ssl_port

    def send_email(self) -> None:
        msg = MIMEMultipart()
        if self.file:
            file_name = os.path.split(self.file)[-1]
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！！')
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                # base64.b64encode(file_name.encode()).decode()
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                att["Content-Disposition"] = 'attachment; filename="%s"' % (new_file_name)
                msg.attach(att)
        msg.attach(MIMEText(self.content))
        msg['Subject'] = self.title
        msg['From'] = self.username
        msg['To'] = ','.join(self.recv)
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
            pass
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')
        self.smtp.quit()


def mail():
    new_html = get_htmlPath()
    htmlPath = new_html.html_list()
    m = SendEmail(
        username='18001098773@163.com',
        passwd='FEHRWZTRHUDPIWZM',
        recv=['zhangxu01@sinoiov.com'],
        title='测试报告',
        content='发送邮件',
        file=f'reports//{htmlPath}',
        ssl=True,
    )
    m.send_email()
