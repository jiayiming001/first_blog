# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.six import python_2_unicode_compatible
from django.db import models
@python_2_unicode_compatible
class comments(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey("article.Article")

    def __str__(self):
        return self.text[:20]
# Create your models here.
