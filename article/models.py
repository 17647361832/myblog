
# Create your models here.
from django.db import models

# 导入内建的User模型
from django.contrib.auth.models import User
from django.utils import timezone

# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者。参数on_delete 用于指定数据删除的方式，避免两个关联表数据不一致
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题
    title = models.CharField(max_length=100)

    # 文章正文
    body = models.TextField()

    created = models.DateTimeField(default=timezone.now())

    # 文章更新时间 参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    # 内部类class Meta用于给model定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # ’-created‘ 表明数据应该以倒叙排列
        ordering = ('-created',)

    def __str__(self):
        return self.title

    # 内部类Meta中的ordering定义了数据的排列方式。-created表示将以创建时间的倒序排列
    # ，保证了最新的文章总是在网页的最上方。注意ordering是元组，括号中只含一个元素时不
    # 要忘记末尾的逗号。
    #
    # __str__方法定义了需要表示数据时应该显示的名称。给模型增加
    # __str__方法是很重要的，它最常见的就是在Django管理后台中做为对象的显示值。因此应该
    # 总是返回一个友好易读的字符串。后面会看到它的好处。