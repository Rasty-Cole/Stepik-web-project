import gunicorn

def app(environ, start_response):
    data = environ['QUERY_STRING']
    lines = data.split('&')

    result = ""
    for line in lines:
        result = result + line + "\n"
#        if line != lines[-1]: result = result + "\n"

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(result)))
    ]
    start_response(status, response_headers)
    return iter([result])