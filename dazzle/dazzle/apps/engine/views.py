from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotModified
from django.views.decorators.csrf import csrf_exempt
from apps.engine.converter import Converter 
from apps.dztemplate.manager import upload_image

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
		return HttpResponseBadRequest

	requestType = request.POST.get('requestType')

	if requestType == 'updateImage':
		return update_image(request, template_name)

	if requestType == 'updateText':
		return update_text(request, template_name)

	return HttpResponse("unknown request")

def update_image(request, template_name):
	save_id = request.POST.get('id')

	if not request.FILES or not save_id:
		return HttpResponseBadRequest

	for f in request.FILES.getlist('file'):
		success = upload_image(template_name, f)

		if not success:
			return HttpResponseNotModified

		converter = Converter(template_name, 'index.html')
		
		location = converter.replace_image(save_id, f.name)

		if location is not None:
			converter.commit_template()
			return HttpResponse(location)

		break

	return HttpResponseNotModified

def update_text(request, template_name):
	save_id = request.POST.get('id')

	save_data = request.POST.get('value') 

	converter = Converter(template_name, 'index.html')

	success = converter.update_text(save_id, save_data)

	if success:
		converter.commit_template()

	return HttpResponse('got ' + save_id + ' ' + save_data)

def upload(request, template_name): 
	converter = Converter(template_name, 'index.html')
	converter.run_upload_engine()

	return HttpResponse(template_name + ' uploaded')

	
