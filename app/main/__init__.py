# -*- coding: utf-8 -*-
# @Author: huerke
# @Date:   2016-09-03 10:55:15
# @Last Modified by:   huerke
# @Last Modified time: 2016-09-03 10:58:28
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
