
from django.template.loader import render_to_string
import urllib2 
import utils.constants as Constants

def get_template_as_string(template_name, file_name):

	response = urllib2.urlopen(Constants.S3_TEMPLATE_URL + template_name + '/' + file_name)
	html_string = response.read() 
	return html_string