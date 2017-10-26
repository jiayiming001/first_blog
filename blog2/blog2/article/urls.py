from django.conf.urls import url
from views import IndexView,detail,archivers,category
from . import views


app_name = 'article'

urlpatterns = [
               url(r'^index/$', view=IndexView.as_view(), name='index'),
               #url(r'^index/$', IndexView, name='index'),
               #url(r'^(?P<pk>\d+)/$',view=DetailView.as_view(),name='detail'),
               url(r'^(?P<pk>\d+)/$',view=detail,name='detail'),
               url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',view=archivers.as_view(), name='archives'),
               url(r'^category/(?P<pk>[0-9]+)/$',view=views.category.as_view(), name='category'),
               url(r'^about/$',views.AboutView),
               url(r'^listpic/$',views.Listpic),
               url(r'^newlistpic/$',views.Newlistpic),
]