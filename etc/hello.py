bind = '0.0.0.0:8080'
pythonpath = '/home/box/web'

def app(environ, start_response):
    result = ""
    for line in environ['QUERY_STRING'].split('&'):
        result = result + line + "\n"

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(result)))
    ]
    start_response('200 OK', response_headers)
    return iter([result.encode('utf-8')])