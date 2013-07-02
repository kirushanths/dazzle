
from django.template.loader import render_to_string

def get_template_string():
	html_string = render_to_string('dztemplate/home.html')
	return html_string