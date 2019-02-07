# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: P♂boy
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 17647361832@163.com
@Software: Pycharm
@File: urls.py
@Time: 2019/2/5 11:24
@Desc:
"""


# 引入path
from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'article'
urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name="article_create"),
    path('article-delete/<int:id>/', views.article_delete, name="article_delete"),
    path('article-update/<int:id>/', views.article_update, name="article_update"),
]