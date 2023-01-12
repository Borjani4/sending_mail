from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
import config


# создаем функцию с параметрами: кому отпр. тема сообщ., и текст сообщения
def send_email(to_addr, subject, text):
    msg = MIMEMultipart
    msg['From'] = config.login
    msg['To'] = config.login
    msg['subject'] = subject
    # прикрепляем к нашему письму сам текст
    msg.attach(MIMEText(text, 'plain'))
    # создаем сервер,авторизоваться в нем отправить сообщение, и выдти
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.ehlo(config.login)
    server.login(config.login, login_parol_mail.password)
    server.auth_plain()
    server.send_message(msg)
    server.quit()


send_email(config.login, 'python is best', 'Hello world')
