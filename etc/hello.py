bind = '0.0.0.0:8000'
pythonpath = '/mnt/d/Programs-PartII/Stepik.org/Web-technology/web-project-stepik/etc'

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
