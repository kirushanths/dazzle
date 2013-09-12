from django.conf.urls import patterns, url

urlpatterns = patterns('apps.core.views',
	url(r'^$', 'home', name='home'),
)
