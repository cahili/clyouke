# -*- coding: utf-8 -*-
# @Author: huerke
# @Date:   2016-09-03 10:40:30
# @Last Modified by:   huerke
# @Last Modified time: 2016-09-03 15:53:41
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
