from pyquery import PyQuery
import urlparse   
import utils.constants as Constants
from lxml import etree
from dztemplate.manager import get_template_as_string
from dztemplate.manager import save_template
import os

# MAIN ENGINE
class Converter:

	def __init__(self, template_name, file_name):
		template_string = get_template_as_string(template_name, file_name)
		self.html_obj = PyQuery(template_string.decode('utf-8'))
		self.file_name = file_name
		self.template_name = template_name

	def run_upload_engine(self):
		self.insert_element_tags()
		self.commit_template()

	def run_edit_engine(self):
		self.replace_local_links() 
		self.include_scripts()

	def get_converted_html(self):
		final_html =  '<html>' + self.html_obj.html(method='html') + '</html>'
		return final_html.encode('utf-8')
 
	def commit_template(self):
		save_template(self.template_name, self.file_name, self.get_converted_html(), False)
 

	# INCLUDE SCRIPTS FUNCTIONS
	def include_scripts(self): 
		html_obj = self.html_obj

		self.add_scripts([Constants.JQUERY_URL] + Constants.HALLO_JS_URLS + [Constants.ENGINE_JS_URL]) 
		self.add_css(Constants.FONTAWESOME_CSS_URL)
	

	def add_css(self, source):
		html_obj = self.html_obj
		src_str = '<link type="text/css" href="' + source + '" rel="stylesheet"></link>'
		html_obj('head').append(src_str) 

	def add_scripts(self, sources):
		html_obj = self.html_obj 
		src_str = "";
		for src in sources:
			src_str += '<script type="text/javascript" src="' + src + '"></script>'

		html_obj('head').prepend(src_str)
 
 	# TAG FUNCTIONS
 	def insert_element_tags(self): 

 		self.dzid = 0
 		def assign_tag(i, this):

 			self.dzid += 1

 			if element_is_type(this, ['script', 'title', 'head', 'header', 'body', 'footer', 'link', 'style', 'meta']):
 				return 
	
			# wrap text elements
			if this.text is not None and len(this.text.strip(' \t\n\r')) > 0:
				new_element = self.new_text_element(this.text, self.dzid)
				this.text = ''
				this.insert(0, new_element)
				self.dzid += 1

			if this.tail is not None and len(this.tail.strip(' \t\n\r')) > 0:
				new_element = self.new_text_element(this.tail, self.dzid)
				this.tail = ''
				this.addnext(new_element)
				self.dzid += 1

			this.set('dzid', str(self.dzid))

 		html_obj = self.html_obj
 		html_obj('*').each(assign_tag)

	# TEXT FUNCTIONS
	def update_text(self, target, value):
		html_obj = self.html_obj
   
		elements = html_obj('div').filter('[dzid="' + target + '"]')  

		for e in elements:  
	 		pq = PyQuery(e)
	 		pq.empty()
	 		pq.append(value)
	 		
	def new_text_element(self, text, ident):
		element = etree.Element('div')
		element.set('dztype', 'text') 
		element.set('dzid', str(ident))
		element.text = text
		return element

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

			if is_absolute(value):
				continue

			file_name, file_extension = os.path.splitext(value)
			if file_extension == '' or file_extension.find('.html') > 0:
				continue

			value = location + value
			e.set(attr, value)
	  

# HELPER FUNCTIONS
def unique_text_id(num):
	return 'dztxt' + str(num)

def is_absolute(url):
	return bool(urlparse.urlparse(url.strip()).scheme)

def element_is_type(element,type_arr):
	for e_type in type_arr:
		if PyQuery(element).is_(e_type):
			return True
	return False


