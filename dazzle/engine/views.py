from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse 
from engine.converter import Converter

def convert(request, template_name):
  
  	edit_mode = True

	converter = Converter(template_name, 'index.html', edit_mode)
	
	converter.run_engine() 

	converted_html_string = converter.get_converted_html()

	template = Template(converted_html_string)

	context = Context(request)

	return HttpResponse(template.render(context)) 

def update(request, template_name):

	if request.method != 'POST':
		return HttpResponse("error")

	save_data = request.POST.get('data')
	
	return HttpResponse(save_data)
