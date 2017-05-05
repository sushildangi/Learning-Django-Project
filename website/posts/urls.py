from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [

    # /posts/
    url(r'^$', views.post_list, name='list'),
    url(r'^create/$', views.post_create, name='create'),
    url(r'^detail/(?P<slug>[-\w]+)/$', views.post_detail, name='detail'),
    url(r'^detail/(?P<slug>[-\w]+)/edit/$', views.post_update, name='update'),
    url(r'^detail/(?P<slug>[-\w]+)/delete/$', views.post_delete, name='delete'),
]
