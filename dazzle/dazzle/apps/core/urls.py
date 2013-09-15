from django.conf.urls import patterns, url
from django.conf.urls.defaults import *
from django.contrib import auth

urlpatterns = patterns('apps.core.views',
	url(r'^$', 'home', name='home')
)

urlpatterns += patterns('',
	url(r'^accounts/', include('apps.core.accounts.urls')),
	url(r'^dashboard/', include('apps.core.dashboard.urls'))
)
