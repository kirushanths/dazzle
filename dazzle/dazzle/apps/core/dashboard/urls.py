from django.conf.urls import patterns, url
from django.conf.urls.defaults import *
from django.contrib import auth

urlpatterns = patterns('apps.core.dashboard.views',
	url(r'^$', 'home', name='home')
)

urlpatterns += patterns('',
)