import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from config import Config


class SendEmail:
    def __init__(self):
        pass

    config = Config.get_instance()
    user_name = config.get_str('email', 'user_name')
    user_password = config.get_str('email', 'password')

    subject = 'fx login'
    sender = config.get_str('email', 'sender')
    receiver = config.get_str('email', 'receiver')
    smtp_server = config.get_str('email', 'smtp_server')

    def send_msg(self, msg_content):
        msg = MIMEText(msg_content, 'text', 'UTF-8')
        msg['Subject'] = Header(self.subject, 'utf-8')

        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        smtp.login(self.user_name, self.user_password)
        smtp.sendmail(self.sender, self.receiver, msg.as_string())
        smtp.quit()


if __name__ == '__main__':
    email = SendEmail()
    email.send_msg("20171019 test")
