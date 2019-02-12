# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: P♂boy
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 17647361832@163.com
@Software: Pycharm
@File: forms.py
@Time: 2019/2/12 10:55
@Desc:
"""
from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']