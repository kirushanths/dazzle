from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse 
from engine.converter import Converter

def convert(request):
  
  	edit_mode = True

	converter = Converter('thinksimple', 'index.html', edit_mode)
	
	converter.run_engine() 

	converted_html_string = converter.get_converted_html()

	template = Template(converted_html_string)

	context = Context(request)

	return HttpResponse(template.render(context))
