# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: P♂boy
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 17647361832@163.com
@Software: Pycharm
@File: urls.py
@Time: 2019/2/12 10:38
@Desc:
"""
from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]