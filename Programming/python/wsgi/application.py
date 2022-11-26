def main(environ, start_response):

    status = '200 OK'
    response_body = 'IP: {e[REMOTE_ADDR]}\nMethod: {e[REQUEST_METHOD]}\n'.format(e=environ)
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body.encode()]

def iter(environ, start_response):

    status = '200 OK'
    response_body = ['{0}: {1}\n'.format(k, v).encode() for k,v in environ.items()]
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(sum([len(x) for x in response_body])))
    ]

    start_response(status, response_headers)
    return response_body
