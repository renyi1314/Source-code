import socket
from multiprocessing import Process
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return "hello,world"


httpd = make_server("", 8888, application)
print(application)
print("server start")
httpd.serve_forever()
