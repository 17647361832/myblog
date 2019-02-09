from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from userprofile.forms import UserLoginForm, UserRegisterForm, ProfileForm
from userprofile.models import Profile


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

def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # 保存好数据后立即登录并返回博客列表页面
            login(request, new_user)
            return redirect("article:article_list")
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


@login_required(login_url='/userprofile/login')
def user_delete(request, id):
    user = User.objects.get(id=id)
    if request.user == user:
        logout(request)
        user.delete()
        return redirect('article:article_list')

    else:
        return HttpResponse("您没有删除的权限")


# 编辑用户信息
@login_required(login_url='/userprofile/login/')
def profile_edit(request, id):
    user = User.objects.get(id=id)
    # user_id是OneToOneField自动生成的字段
    profile = Profile.objects.get(user_id=id)

    if request.method == 'POST':
        # 验证修改数据者是否为本人
        if request.user != user:
            return HttpResponse("你没有权限修改次用户信息")

        # 上传的文件保存在 request.FILES 中，通过参数传递给表单类
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            # 取得清洗后的合法数据
            profile_cleaned_data = profile_form.cleaned_data
            profile.phone = profile_cleaned_data['phone']
            profile.bio = profile_cleaned_data['bio']
            if 'avatar' in request.FILES:
                profile.avatar = profile_cleaned_data['avatar']
            profile.save()
            return redirect("userprofile:edit", id=id)

        else:
            return HttpResponse("注册表单输入有误,请重新输入")

    elif request.method == "GET":
        profile_form = ProfileForm()
        context = {'profile_form': profile_form, 'profile': profile, 'user': user}
        return render(request, 'userprofile/edit.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")