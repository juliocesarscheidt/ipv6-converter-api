# -*- coding: utf-8 -*-
from bottle import Bottle, route, run, request, response, HTTPResponse
import re
import os
from ipv6_converter import convert_ipv6, valid_ipv6, valid_ipv4, valid_mac

PORT = os.environ.get('PORT', 5000)
HOST = os.environ.get('HOST', '0.0.0.0')
DEBUG = os.environ.get('DEBUG', True)

# Instancia do app
app = Bottle()

# Definição de rotas
@app.route('/api/v1/convert_ipv6', method = 'GET')
def main_convert_ipv6():
  response.content_type = 'application/json'

  ipv6_prefix = request.query.get('ipv6_prefix', '')
  mac = request.query.get('mac', '')

  if not ipv6_prefix or not mac:
    return HTTPResponse({ 'message': 'Invalid parameters' }, 400)

  mac = mac.replace(':', '-')

  ipv6 = convert_ipv6(ipv6_prefix, mac)

  if not ipv6:
    return HTTPResponse({ 'message': 'Invalid IPv6 or MAC Address' }, 400)

  return HTTPResponse({ 'message': ipv6 }, 200)

@app.route('/api/v1/valid_ipv6', method = 'GET')
def main_valid_ipv6():
  response.content_type = 'application/json'

  ipv6 = request.query.get('ipv6', '')

  if not ipv6:
    return HTTPResponse({ 'message': 'Invalid parameters' }, 400)

  if not valid_ipv6(ipv6):
    return HTTPResponse({ 'message': False }, 200)

  return HTTPResponse({ 'message': True }, 200)

@app.route('/api/v1/valid_ipv4', method = 'GET')
def main_valid_ipv4():
  response.content_type = 'application/json'

  ipv4 = request.query.get('ipv4', '')

  if not ipv4:
    return HTTPResponse({ 'message': 'Invalid parameters' }, 400)

  if not valid_ipv4(ipv4):
    return HTTPResponse({ 'message': False }, 200)

  return HTTPResponse({ 'message': True }, 200)

@app.route('/api/v1/valid_mac', method = 'GET')
def main_valid_mac():
  response.content_type = 'application/json'

  mac = request.query.get('mac', '')

  if not mac:
    return HTTPResponse({ 'message': 'Invalid parameters' }, 400)

  mac = mac.replace(':', '-')

  if not valid_mac(mac):
    return HTTPResponse({ 'message': False }, 200)

  return HTTPResponse({ 'message': True }, 200)

run(app, host = HOST, port = PORT, debug = DEBUG)
