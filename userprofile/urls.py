# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: P♂boy
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 17647361832@163.com
@Software: Pycharm
@File: urls.py
@Time: 2019/2/7 15:36
@Desc:
"""
from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns=[
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]