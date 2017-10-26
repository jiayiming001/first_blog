# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Article,Category
from django.views.generic import ListView
from comments.forms import CommentForm
import markdown
from django.shortcuts import render
from django.shortcuts import get_object_or_404
import markdown2 
from django.shortcuts import render_to_response

"""def IndexView(request):
    object_list = Article
    object_cate = Category
    return render_to_response('index.html',locals())

"""
class IndexView(ListView):
    template_name = 'index.html'    # 指定需要渲染的模板
    model = Article
    ordering = ['-create_time']
    paginate_by = 1
    context_object_name =  "article_list" # 指定模板中需要使用的上下文对象的名字

    def get_queryset(self): #重写get_queryset，过滤status不是0的数据，这里过滤的是Article数据
        return super(IndexView,self).get_queryset().filter(status=0)


    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}
        left = [ ]
        right = [ ]
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_number = int(page.number) #当前页码
        total_pages = int(paginator.num_pages) #所有页数
        page_range = list(paginator.page_range) #所有页码的列表

        if page_number == 1:
            right = page_range[page_number:page_number+2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number-3) if (page_number - 3) > 0 else 0:page_number-1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            right = page_range[page_number:page_number + 2]
            left = page_range[(page_number-3) if (page_number - 3) > 0 else 0:page_number-1]
            if  left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }

        return data

'''
    def get_context_data(self, **kwargs):  #添加除去model外的数据库数据
        context = super(IndexView, self).get_context_data(**kwargs)  #重写get_context_data,获取context字典
        cate = Category.objects.all() #获取分类模型的所有数据，保存到变量cate
        context.update({'cate':cate}) # 调用字典的方法update，将cate中的数据以‘cate'为key,添加到字典中
        return context                # 返回添加完数据的字典

'''
#class DetailView(DetailView):
 #   model = Article
  #  template_name = 'detail.html'
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.increase_view() #阅读数加1
    article.article = markdown.markdown(article.article,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = article.comments_set.all()
    context = {'article':article,
               'form':form,
               'comment_list':comment_list,
    }
    return render(request, 'detail.html', context=context)

class archivers(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article_list'
    def get_queryset(self, *args, **kwargs):
        return super(archivers, self).get_queryset().filter(create_time__year=self.kwargs.get('year'), create_time__month=self.kwargs.get('month'))

'''
def archivers(request, year, month):
    article_list = Article.objects.filter(create_time__year=year,
                                          create_time__month=month).order_by('-create_time')
    return render(request, 'index.html', context={'article_list':article_list})
'''

class category(ListView):
    model = Article
    template_name = 'index.html'
    ordering = ['-create_time']
    context_object_name = "article_list"

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(category,self).get_queryset().filter(category=cate)


'''
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'index.html', context={'article_list':article_list})
'''




def AboutView(request):
    return render(request, 'about.html')

def Listpic(request):
    return render(request, 'listpic.html')

def Newlistpic(request):
    return render(request, 'newslistpic.html')
# Create your views here.
