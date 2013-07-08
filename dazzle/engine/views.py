from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
from engine.converter import Converter 

def convert(request, template_name):

	converter = Converter(template_name, 'index.html')
	
	converter.run_edit_engine() 

	converted_html_string = converter.get_converted_html()

	template = Template(converted_html_string)

	context = Context(request)

	return HttpResponse(template.render(context)) 

@csrf_exempt
def update(request, template_name):

	if request.method != 'POST':
		return HttpResponse("error")

	save_id = request.POST.get('id')
	save_data = request.POST.get('value') 

	converter = Converter(template_name, 'index.html')

	converter.update_text(save_id, save_data)

	converter.commit_template()

	return HttpResponse('got ' + save_data)
