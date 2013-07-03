from pyquery import PyQuery
import urlparse 

def convert_engine(html_string):

	html_obj = PyQuery(html_string.decode('utf-8'))

	replace_local_links(html_obj)

	return_html =  '<html>' + html_obj.html() + '</html>'

	return return_html.encode('utf-8')

def replace_local_links(html_obj):
	replace_link(html_obj, 'src')
	replace_link(html_obj, 'href')


def replace_link(html_obj, attr):

	location = 'http://s3.amazonaws.com/dazzledev/templates/thinksimple/'

	elements = html_obj('*').filter('[' + attr + ']')
	for e in elements:
		value = e.get(attr);

		if (not is_absolute(value)):  
			value = location + value
			e.set(attr, value)

def is_absolute(url):
	return bool(urlparse.urlparse(url).scheme)
  




