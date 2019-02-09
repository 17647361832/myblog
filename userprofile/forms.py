# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: P♂boy
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 17647361832@163.com
@Software: Pycharm
@File: forms.py
@Time: 2019/2/7 13:45
@Desc:
"""

from django import forms

from django.contrib.auth.models import User

from userprofile.models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

# 用户注册表单类
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email']


    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')

        else:
            raise forms.ValidationError("密码输入不一致，请重试")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'avatar', 'bio')