from markdown import markdown
import markdown
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from comment.models import Comment
from .models import ArticlePost
from django.db.models import Q

# 文章列表函数
def article_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    # 用户搜索逻辑，请求中有search，则走次逻辑
    if search:
        if order == 'total_views':
        # 用q对象进行联合搜索
            article_list = ArticlePost.objects.filter(
                Q(title__contains=search)|  # icontains不区分分大小写，contains区分大小写
                Q(body__icontains=search)
            ).order_by('-total_views')

        else:
            article_list = ArticlePost.objects.filter(
                Q(title__contains=search) |
                Q(body__icontains=search)
            )
    # 根据GET请求中查询条件
    # 返回不同排序的对象数组
    else:
        search = ''
        if order == 'total_views':
            article_list = ArticlePost.objects.all().order_by('-total_views')
        else:
            article_list = ArticlePost.objects.all()
    paginator = Paginator(article_list, 3)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    # 修改此行
    context = {'articles': articles, 'order': order, 'search': search}
    return render(request, 'article/list.html', context)


# 文章详情
def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    # 取出对应文章的评论
    comments = Comment.objects.filter(article=id)

    article.total_views += 1
    article.save(update_fields=['total_views'])
    md = markdown.Markdown(
        extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
            # 目录扩展
            'markdown.extensions.toc',
        ]
    )
    article.body = md.convert(article.body)
    context = {'article': article, 'toc': md.toc, 'comments': comments}
    # 载入模板，并返回context对象p
    return render(request, 'article/detail.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
# 引入刚才定义的ArticlePostForm
from .forms import ArticlePostForm
from django.contrib.auth.models import User

# 检查登陆
@login_required(login_url='/userprofile/login')
def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交时数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            new_article.save()
            return redirect('article:article_list')
        else:
            return HttpResponse("表单内容有误,请重新填写")

    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)

# 检查登陆
@login_required(login_url='/userprofile/login')
def article_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect('article:article_list')

# 检查登陆
@login_required(login_url='/userprofile/login')
def article_update(request, id):
    # 获取文章对象
    article = ArticlePost.objects.get(id=id)
    if request.method =="POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()

            return redirect("article:article_detail", id=id)
        else:
            return HttpResponse("表单内容有误,请重新填写")


    else:
        article_post_form = ArticlePostForm()
        context = { 'article': article, 'article_post_form': article_post_form}
        return render(request, 'article/update.html', context)