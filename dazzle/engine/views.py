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

	requestType = request.POST.get('requestType')

	if requestType == 'updateImage':
		return update_image(request, template_name)

	if requestType == 'updateText':
		return update_text(request, template_name)

	return HttpResponse("unknown request")

def update_image(request, template_name):

	if not request.FILES:
		return HttpResponse("file error")

	#for f in request.FILES.getlist('file'):

	return HttpResponse('update image')

def update_text(request, template_name):
	save_id = request.POST.get('id')

	save_data = request.POST.get('value') 

	converter = Converter(template_name, 'index.html')

	converter.update_text(save_id, save_data)

	converter.commit_template()

	return HttpResponse('got ' + save_id + ' ' + save_data)

def upload(request, template_name): 
	converter = Converter(template_name, 'index.html')
	converter.run_upload_engine()
	return HttpResponse(template_name + ' uploaded')
