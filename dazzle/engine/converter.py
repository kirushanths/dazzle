from pyquery import PyQuery
import urlparse   
import utils.constants as Constants
from lxml import etree
from dztemplate.manager import get_template_as_string
from dztemplate.manager import save_template

# MAIN ENGINE
class Converter:

	def __init__(self, template_name, file_name):
		template_string = get_template_as_string(template_name, file_name)
		self.html_obj = PyQuery(template_string.decode('utf-8'))
		self.file_name = file_name
		self.template_name = template_name

	def run_edit_engine(self):
		self.replace_local_links()
		self.set_text_editable()
		self.include_scripts()

	def get_converted_html(self):
		final_html =  '<html>' + self.html_obj.html(method='html') + '</html>'
		return final_html.encode('utf-8')

	# TEMPLATE FUNCTIONS
	def commit_template(self):
		save_template(self.template_name, self.file_name, self.get_converted_html(), False)

	# UPDATE FUNCTIONS
	def update_text(self, target, value):

		html_obj = self.html_obj
   
		elements = html_obj('*').filter(has_text)  

		num = 1

		for e in elements: 
	 		if target != get_unique_text_id(num):
	 			num += 1
	 			continue

			e.text = value
			break

	# PREVIEW FUNCTIONS

	########## EDIT MODE #########

	# INCLUDE SCRIPTS FUNCTIONS
	def include_scripts(self): 

		def has_js(val):
			e = PyQuery(this)
			source = e.attr('src')

			if source is None: 
				return False

			if source.lower().find(val) != -1:
				return True

		html_obj = self.html_obj

		elements = html_obj('script').filter(lambda: has_js('jquery'))  
		if len(elements) == 0: 
			self.add_jquery() 
		#elements = html_obj('script').filter(lambda: has_js('bootstrap'))  
		#if len(elements) == 0: 
		#	self.add_script(Constants.BOOTSTRAP_JS_URL)
		#	self.add_css(Constants.BOOTSTRAP_CSS_URL)
		self.add_script(Constants.POSHTIP_JS_URL)
		self.add_script(Constants.XEDITABLE_JS_URL)
		self.add_css(Constants.XEDITABLE_CSS_URL)
		self.add_script(Constants.ENGINE_JS_URL)


	def add_css(self, source):
		html_obj = self.html_obj
		src_str = '<link type="text/css" href="' + source + '" rel="stylesheet"></link>'
		html_obj('head').append(src_str) 

	def add_script(self, source):
		html_obj = self.html_obj 
		src_str = '<script type="text/javascript" src="' + source + '"></script>'
		html_obj('body').append(src_str) 

	def add_jquery(self):
		html_obj = self.html_obj 
		src_str = '<script type="text/javascript" src="' + Constants.JQUERY_URL + '"></script>'
		html_obj('head').append(src_str) 
 
	# TEXT FUNCTIONS
	def set_text_editable(self):
 
		html_obj = self.html_obj
   
		elements = html_obj('*').filter(has_text)  

		num = 1

		for e in elements: 
	 		#if len(list(e)) == 0:
	 		e.set('dztype', 'text')
			e.set('dzid', get_unique_text_id(num))
			num += 1

	# REPLACE LINK FUNCTIONS
	def replace_local_links(self):
		self.replace_link('src')
		self.replace_link('href')


	def replace_link(self, attr):

		html_obj = self.html_obj

		location = Constants.S3_TEMPLATE_URL + self.template_name + '/'

		elements = html_obj('*').filter('[' + attr + ']')
		for e in elements:
			value = e.get(attr);

			if (not is_absolute(value)):  
				value = location + value
				e.set(attr, value)
	  

# HELPER FUNCTIONS

def get_unique_text_id(num):
	return 'dztxt' + str(num)

def is_absolute(url):
	return bool(urlparse.urlparse(url.strip()).scheme)

def has_text(i, this):
	if PyQuery(this).is_('script'): 
		return False

	text = PyQuery(this).clone().children().remove().end().text()
		
	if text is None:
		return False

	if (len(text.strip(' \t\n\r')) > 0):
		return True

	return False


