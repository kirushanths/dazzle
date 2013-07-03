
from django.template.loader import render_to_string
import urllib2 

def get_template_as_string():

	response = urllib2.urlopen('http://s3.amazonaws.com/dazzledev/templates/thinksimple/index.html')
	html_string = response.read() 
	return html_string