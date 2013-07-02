from django.conf.urls import patterns, url

urlpatterns = patterns('engine.views',
	url(r'^$', 'convert', name='convert'),
)
