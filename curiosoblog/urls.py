from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    #url(r'^(?P<slug>[\w-]+)/like/$', PostLikeToggle.as_view(), name='like-toggle'),
    #url(r'^api/(?P<slug>[\w-]+)/like/$', PostLikeAPIToggle.as_view(), name='like-api-toggle'),
    #url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.delete, name='delete'),


]
