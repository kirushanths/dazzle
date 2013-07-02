from pyquery import PyQuery

def convert_engine(html_string):

	html_obj = PyQuery(html_string)

	html_obj.append("<body>hello</body>")

	return '<html>' + html_obj.html() + '</html>'
