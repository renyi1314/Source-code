import datetime


# def application(request_dict,response__):
#     if request_dict['name'] == '/favicon.ico':
#         response__('404 Not Found', [])
#         return ''
#     data = str(datetime.datetime.now())
#     response__('200 OK', [('abc', 'hello'), ('Server_Name', '0320'), ('Content-Type', 'text/html; charset=UTF-8')])
#     return data

def application(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/html; charset=UTF-8')])
    return "123"
