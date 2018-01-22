from ..models import Article,Category
from django import template
from django.db.models.aggregates import Count
register = template.Library()

@register.simple_tag
def get_recent_Artilce(num=5):
    return Article.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def archives():
    return Article.objects.dates('create_time','month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)
