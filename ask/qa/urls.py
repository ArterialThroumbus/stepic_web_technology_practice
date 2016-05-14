from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
    url(r'^$', views.test, name='main'),
    url(r'^login/$', views.test, name='login'),
    url(r'^signup/$', views.test, name='signup'),
    url(r'^question/(?P<qid>[^/]+)/$', views.test, name='question'),
    url(r'^ask/$', views.test, name='ask'),
    url(r'^popular/$', views.test, name='popular'),
    url(r'^new/$', views.test, name='new'),
)