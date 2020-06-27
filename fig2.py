from cgi import parse_qs
import template2

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    x = d.get('x', [''])[0]
    y = d.get('y', [''])[0]
    sum, mul = 0, 0
    if '' not in [x, y]:
        x, y= int(x), int(y)
        sum = x + y
        mul = x + y
    response_body = html%{'sum' : sum, 'mul' : mul}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
