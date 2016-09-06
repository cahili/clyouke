# -*- coding: utf-8 -*-
# @Author: huerke
# @Date:   2016-09-03 10:40:30
# @Last Modified by:   huerke
# @Last Modified time: 2016-09-04 22:59:49
from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['CL_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['CL_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
