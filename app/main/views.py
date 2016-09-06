# -*- coding: utf-8 -*-
# @Author: huerke
# @Date:   2016-09-03 10:55:34
# @Last Modified by:   Administrator
# @Last Modified time: 2016-09-05 10:04:29
from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, session
from flask_login import login_required, current_user
from . import main
from .forms import KeyForm
from .. import db
from ..models import Jishuqu, Dagaier
from ..get1024addr import caoliuaddr
domain_name = caoliuaddr
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@main.route('/')
def index():
    return render_template('index.html', domain_name=domain_name)


@main.route('/jishu', methods=['GET', 'POST'])
@login_required
def jishu():
    form = KeyForm()
    result = ''
    if form.validate_on_submit():
        key = form.key.data
        result = Jishuqu.query.filter(
            Jishuqu.title.like('%' + key + '%')).all()
        if not result:
            flash('未找到相关结果')
    return render_template('jishu.html', form=form, result=result, domain_name=domain_name)


@main.route('/dagaier', methods=['GET', 'POST'])
@login_required
def dagaier():
    form = KeyForm()
    result = ''
    if form.validate_on_submit():
        key = form.key.data
        result = Dagaier.query.filter(
            Dagaier.title.like('%' + key + '%')).all()
        if not result:
            flash('未找到相关结果')
    return render_template('dagaier.html', form=form, result=result, domain_name=domain_name)
