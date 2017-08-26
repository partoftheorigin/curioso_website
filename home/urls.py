from django.conf import settings
from django.conf.urls import include, url
from . import views

app_name = 'home'

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view(), name='home'),

    url(r'^guide/$', views.guide, name='guide'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^writeforus/$', views.writeforus, name='writeforus'),
    url(r'^career/$', views.career, name='career'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^curiosoblog/', include("curiosoblog.urls", namespace='curiosoblog')),
    url(r'^$', views.index, name='index'),

]
handler404 = 'curiosoblog.views.handler404'
