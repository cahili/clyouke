# -*- coding: utf-8 -*-
# @Author: huerke
# @Date:   2016-09-03 10:55:54
# @Last Modified by:   huerke
# @Last Modified time: 2016-09-03 15:54:50
from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
