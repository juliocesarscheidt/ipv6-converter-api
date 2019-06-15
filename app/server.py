from bottle import Bottle, route, run, request, response, HTTPResponse
import re
import os
from ipv6_converter import transform_ipv6

PORT = os.environ.get('PORT', '8080')
HOST = os.environ.get('HOST', '0.0.0.0')
DEBUG = os.environ.get('DEBUG', True)

app = Bottle()

@app.route('/api/v1/convert', method='GET')
def test():
  response.content_type = 'application/json'

  ip = request.query.get('ip', '')
  mac = request.query.get('mac', '')

  if not ip or not mac:
    return HTTPResponse({ 'message': 'Invalid parameters' }, 400)

  ipv6 = transform_ipv6(ip, mac)

  if not ipv6:
    return HTTPResponse({ 'message': 'Invalid IPv6 or MAC Address' }, 400)

  return HTTPResponse({ 'message': ipv6 }, 200)

run(app, host=HOST, port=PORT, debug=DEBUG)

# Example
# http://localhost:8080/api/v1/convert?ip=2804-14c-87b5-9199&mac=00-1D-7D-F9-92-85
