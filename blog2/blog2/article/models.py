# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.six import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField("名称", max_length=64)
    create_time = models.DateTimeField("添加时间", auto_now_add=True)
    status = models.IntegerField("状态", default=0)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = "文章分类"

def upload_to_goods_img(instance, filename):
    return 'article/{prefix}_{filename}.{suffix}'.format(prefix='article',
                                                         filename=int(time.time() * 1000),
                                                         suffix=filename.split('.')[-1])



class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name="分类")
    user = models.ForeignKey(User)
    title = models.CharField("标题", max_length=128)
    description = models.CharField("描述", max_length=256, blank=True)
    article = models.TextField("文章")
    create_time = models.DateTimeField("发表时间", auto_now_add=True)
    status = models.IntegerField("状态", default=0)
    img = models.ImageField("图片", upload_to=upload_to_goods_img)
    views = models.PositiveIntegerField(default=0)     # 新增views字段记录浏览量


    def save(self, *args, **kwargs):
        if not self.description:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.description = strip_tags(md.convert(self.article))[:54]
        super(Article, self).save(*args, **kwargs)

    def increase_view (self):  #views+1,并且保存到数据库
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

        # 自定义 get_absolute_url 方法
        # 记得从 django.urls 中导入 reverse 函数
    '''于是 reverse 函数会去解析这个视图函数对应的 URL，我们这里 detail 对应的规则就是 article/(?P<pk>[0-9]+)/ 这个正则表达式，而正则表达式部分会被后面传入的参数 pk 替换，所以，如果 Post 的 id（或者 pk，这里 pk 和 id 是等价的） 是 255 的话，那么 get_absolute_url 函数返回的就是 /post/255/ ，这样 Post 自己就生成了自己的 URL。
    '''
    def get_absolute_url(self):
        return reverse('article:detail', kwargs={'pk':self.pk})

    class Meta:
        verbose_name="文章信息"
        verbose_name_plural="文章信息"
        ordering = ['-create_time']

class Price(models.Model):
    STATUS_CHOICES ={
        ('a',"温州大学"),
        ('b',"温大瓯江"),
        ('c',"温大瓯江理工"),
    }
    price_name = models.CharField("奖项名称",max_length=128)
    get_time = models.DateField("获得时间")
    description = models.TextField("奖项内容")
    give_man = models.CharField("颁发单位", max_length=1,choices=STATUS_CHOICES)

    def __str__(self):
        return self.price_name

    class Meta:
        verbose_name = "个人奖项"
        verbose_name_plural = "个人奖项"



