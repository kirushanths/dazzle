from django.conf.urls import patterns, url
from django.conf.urls.defaults import *
from django.contrib import auth

urlpatterns = patterns('apps.dashboard.views',
	url(r'^$', 'home', name='dashboard_home'),
	url(r'^manager/', 'manager', name='dashboard_manager'),
    url(r'^library/', 'library', name='dashboard_library'),
    url(r'^site/(?P<site_id>\d+)/$', 'site_overview', name='dashboard_site_overview')
)