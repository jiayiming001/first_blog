# -*- coding:utf-8 -*-
from django import forms
from .models import comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['name', 'email', 'url', 'text']
        widgets = {
                    'name': forms.TextInput(attrs={
                        'placeholder': "名字",
                     }),
                     'email': forms.TextInput(attrs={
                         'placeholder': "邮箱",
                     }),
                     'url': forms.TextInput(attrs={
                         'placeholder': "网址",
                    }),
                    'text': forms.Textarea(attrs={
                        'placeholder': "请留下您的评论！"
                    })
                 }