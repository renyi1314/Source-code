import datetime
# class Application:
#
#     def __call__(self, environ, start_response):
#         start_response("HTTP/1.1 200 OK", [("ServerName", "MyWebApplication"), ("content-type", "text/html")])
#         data = datetime.datetime.now().strftime("%Y年%m月%d日")
#         print(data)
#         return data

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return "hello,world"

    # def __call__(self, environ, start_response):
    #     set_script_prefix(get_script_name(environ))
    #     signals.request_started.send(sender=self.__class__, environ=environ)
    #     request = self.request_class(environ)
    #     response = self.get_response(request)
    #
    #     response._handler_class = self.__class__
    #
    #     status = '%d %s' % (response.status_code, response.reason_phrase)
    #     response_headers = list(response.items())
    #     for c in response.cookies.values():
    #         response_headers.append(('Set-Cookie', c.output(header='')))
    #     start_response(status, response_headers)
    #     if getattr(response, 'file_to_stream', None) is not None and environ.get('wsgi.file_wrapper'):
    #         response = environ['wsgi.file_wrapper'](response.file_to_stream)
    #     return response
