# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: P♂boy
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 17647361832@163.com
@Software: Pycharm
@File: froms.py
@Time: 2019/2/7 13:45
@Desc:
"""

from django import forms

from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()