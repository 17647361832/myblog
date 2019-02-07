from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from userprofile.froms import UserLoginForm


def user_login(request):
    if request.method == "POST":
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个user对象
            user = authenticate(username=data['username'], password=data['password'])
            # authenticate()方法验证用户名称和密码是否匹配，如果是，则将这个用户数据返回。
            if user:
                # 将用户数据保存在session中，实现的登陆动作
                login(request, user)
                return redirect("article:article_list")
            else:
                return HttpResponse("账号或密码输入有误,请重新输入")


        else:
            return HttpResponse("账号或密码输入不合法")


    elif request.method =="GET":
        user_login_form = UserLoginForm()
        context = {'from': user_login_form}
        return render(request, 'userprofile/login.html', context)

    else:
        return HttpResponse("请使用GET或POST请求数据")


def user_logout(request):
    logout(request)
    return redirect("article:article_list")