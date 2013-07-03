from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse 
from dztemplate.manager import get_template_as_string
from engine.converter import convert_engine

def convert(request):

	html_string = get_template_as_string()

	converted_html_string = convert_engine(html_string);

	template = Template(converted_html_string)

	context = Context(request)

	return HttpResponse(template.render(context))
