# -*- coding: utf-8 -*-
# @Author: huerke
# @Date:   2016-09-03 10:55:43
# @Last Modified by:   huerke
# @Last Modified time: 2016-09-03 11:21:34
from flask_wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError


class KeyForm(Form):
    key = StringField('请输入标题关键字', validators=[Required()])
    submit = SubmitField('提交')
