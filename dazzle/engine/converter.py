from pyquery import PyQuery
import urlparse   
import utils.constants as Constants

# MAIN ENGINE
def convert_engine(html_string):

	html_obj = PyQuery(html_string.decode('utf-8'))

	replace_local_links(html_obj)

	include_scripts(html_obj)

	set_text_editable(html_obj) 

	return_html =  '<html>' + html_obj.html() + '</html>'

	return return_html.encode('utf-8')


# INCLUDE SCRIPTS FUNCTIONS
def include_scripts(html_obj):
	elements = html_obj('script').filter(lambda: has_js('jquery'))  
	#if len(elements) == 0: 
	#	add_script(html_obj, '../static/libs/jquery-1.9.1.min.js')
	# TEMPORARY: bootstrap only supports jquery 1.7+
	add_script(html_obj, Constants.JQUERY_URL)

	elements = html_obj('script').filter(lambda: has_js('bootstrap'))  
	if len(elements) == 0: 
		add_script(html_obj, Constants.BOOTSTRAP_JS_URL)
		add_css(html_obj,  Constants.BOOTSTRAP_CSS_URL)

	add_css(html_obj, Constants.XEDITABLE_CSS_URL)
	add_script(html_obj, Constants.XEDITABLE_JS_URL)
	add_script(html_obj, Constants.ENGINE_JS_URL)

def add_css(html_obj, source):
	src_str = '<link type="text/css" href="' + source + '" rel="stylesheet"></link>'
	html_obj('head').append(src_str)
	return True

def add_script(html_obj, source): 
	src_str = '<script type="text/javascript" src="' + source + '">/////</script>'
	html_obj('body').append(src_str) 

def has_js(val):
	e = PyQuery(this)
	source = e.attr('src')

	if source is None: 
		return False

	if source.lower().find(val) != -1:
		return True
 
# TEXT FUNCTIONS
def set_text_editable(html_obj):
	elements = html_obj('*').filter(has_text)  

	unique_id = 'dztxt'
	num = 1

 	for e in elements:
 		e.set('dztype', 'text')
 		e.set('dzid', unique_id + str(num))
 		num += 1


def has_text(i, this):
	text = PyQuery(this).clone().children().remove().end().text()
	
	if text is None:
		return False

	if (len(text.strip(' \t\n\r')) > 0):
		return True;

	return False

# REPLACE LINK FUNCTIONS
def replace_local_links(html_obj):
	replace_link(html_obj, 'src')
	replace_link(html_obj, 'href')


def replace_link(html_obj, attr):

	location = Constants.S3_TEMPLATE_URL + 'thinksimple/'

	elements = html_obj('*').filter('[' + attr + ']')
	for e in elements:
		value = e.get(attr);

		if (not is_absolute(value)):  
			value = location + value
			e.set(attr, value)

def is_absolute(url):
	return bool(urlparse.urlparse(url.strip()).scheme)
  




