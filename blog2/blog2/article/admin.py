# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Article
from models import Category,Price

admin.site.site_header = "小贾的blog"
admin.site.site_title = "小贾的blog"

class ArticleAdmin(admin.ModelAdmin):
    #控制展示字段
    list_display = ['title', 'create_time', 'description']
    #可查询的字段
    search_fields = ['title', 'create_time']
    #actions操作动作
    actions = None

    #重写过滤显示，只显示status=0的信息
    def get_queryset(self, request):
        queryset = super(admin.ModelAdmin,self).get_queryset(request)
        return queryset.filter(status=0)

    #重写admin删除的方法（admin删除时调用的是delete_model,修改model为逻辑删除
    def delete_model(self, request, obj):
        obj.status = 1
        obj.save()

    class Media:
        js = (
            '/static/kindeditor/kindeditor-min.js',
            '/static/kindeitor/lang/zh_CN.js',
            '/static/kindeditor/config.js'
        )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'status']
    search_fields = ['name', 'create_time']
    actions = None

    def get_queryset(self, request):
        queryset = super(admin.ModelAdmin, self).get_queryset(request)
        return queryset.filter(status=0)


    def delete_model(self, request, obj):
        obj.status = 1
        obj.save()



class PriceAdmin(admin.ModelAdmin):
    list_display = ['price_name', 'get_time', 'description']
    search_fields = ['price_name', 'get_time',]
    actions = None

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Price, PriceAdmin)
# Register your models here.
