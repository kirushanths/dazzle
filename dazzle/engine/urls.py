from django.conf.urls import patterns, url

urlpatterns = patterns('engine.views',
	url(r'update/(?P<template_name>.+)/$', 'update', name='update'),
	url(r'(?P<template_name>.+)/$', 'convert', name='convert'),
)
