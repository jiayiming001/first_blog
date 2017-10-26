# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import  get_object_or_404,redirect,render
from article.models import Article
from .forms import CommentForm
from .models import comments
# Create your views here.

def article_comments(request, article_pk):
    artilce = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = artilce
            comment.save()
            return redirect(artilce)
        else:
            comment_list = artilce.comment_set.all()
            context = {
                'post':artilce,
                'form':form,
                'comment_list':comment_list
            }
            return render(request, 'detail.html', context=context)
    return redirect(artilce)