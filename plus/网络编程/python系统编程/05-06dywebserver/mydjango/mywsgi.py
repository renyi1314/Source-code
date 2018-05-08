from datetime import datetime


# def applictaion(request_dict, start_response):
#     if request_dict['name'] == '/favicon.ico':
#         start_response('404 Not Found', [])
#         return ''
#     n1 = datetime.now()
#     data = n1.strftime('%Y年%m月%d日 %H:%M:%S')
#     start_response('200 OK', [('abc', 'hello'), ('Server_Name', '0320'), ('Content-Type', 'text/html; charset=UTF-8')])
#     return data


def application(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/html; charset=UTF-8')])
    return 123
