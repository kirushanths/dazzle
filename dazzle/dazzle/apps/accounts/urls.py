from django.conf.urls import patterns, url
from django.conf.urls.defaults import *
from django.contrib import auth

urlpatterns = patterns('apps.accounts.views',
	url(r'^login/$', 'login', name="login"),
	url(r'^logout/$', 'logout', name="logout"),
	url(r'^register/$', 'register', name="register")
)

urlpatterns += patterns('',
)