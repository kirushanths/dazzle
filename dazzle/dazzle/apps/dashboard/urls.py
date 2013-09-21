from django.conf.urls import patterns, url
from django.conf.urls.defaults import *
from django.contrib import auth

urlpatterns = patterns('apps.dashboard.views',
	url(r'^$', 'home', name='home'),
	url(r'^manager/', 'manager', name='manager'),
    url(r'^library/', 'library', name='library'),
    url(r'^site/(?P<site_id>\d+)/$', 'site_overview', name='overview')
)