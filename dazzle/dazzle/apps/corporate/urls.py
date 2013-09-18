from django.conf.urls import patterns, url
from django.conf.urls.defaults import *
from django.contrib import auth

urlpatterns = patterns('apps.corporate.views',
	url(r'^$', 'home', name='home')
)
