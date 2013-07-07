from django.template.loader import render_to_string
import urllib2 
import utils.constants as Constants
from boto import connect_s3
from boto.s3.key import Key 

def get_template_as_string(template_name, file_name):

	response = urllib2.urlopen(Constants.S3_TEMPLATE_URL + template_name + '/' + file_name)
	html_string = response.read() 
	return html_string

def save_template(template_name, file_name, template_string,  is_original):
	conn = connect_s3(Constants.S3_ACCESS_KEY, Constants.S3_SECRET_KEY)
	bucket = conn.get_bucket(Constants.S3_BUCKET)

	k = Key(bucket)
	#k.key = Constants.S3_TEMPLATE_FOLDER + '/test/test.html'
	k.key = Constants.S3_TEMPLATE_FOLDER + '/' + template_name + "/" + file_name
	k.set_contents_from_string(template_string)
	k.set_acl('public-read')
