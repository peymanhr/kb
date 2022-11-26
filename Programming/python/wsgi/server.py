import application
from wsgiref.simple_server import make_server

#httpd = make_server ('localhost', 8051, application.main)
httpd = make_server ('localhost', 8051, application.iter)
#httpd.handle_request()
httpd.serve_forever()
