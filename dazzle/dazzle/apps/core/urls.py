from django.conf.urls import patterns, url
from django.conf.urls.defaults import *
from django.contrib import auth

urlpatterns = patterns('apps.core.views',
	url(r'^$', 'home', name='home'),
	url(r'^accounts/login/$', 'login', name="login"),
	url(r'^accounts/logout/$', 'logout', name="logout"),
	url(r'^accounts/register/$', 'register', name="register")
)

urlpatterns += patterns('',
)
