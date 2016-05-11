

def application(environ, start_response):
	data = ''
	for q in environ['QUERY_STRING'].split('&'):
		data += "{0}\r\n".format(q)
	start_response('200 OK', [('Content-type','text/plain')])
	return [data]