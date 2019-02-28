import urllib, urllib2
import json


host = 'http://apifreelat.market.alicloudapi.com'
path = '/whapi/json/aliweather/briefforecast3days'
method = 'POST'
appcode = 'aac7d47744de4c73b4f98d81aad05922'
querys = ''
bodys = {}
url = host + path

bodys['lat'] = '''30.2741'''
bodys['lon'] = '''120.1551'''
bodys['token'] = '''443847fa1ffd4e69d929807d42c2db1b'''
post_data = urllib.urlencode(bodys)


def weather_API():
    request = urllib2.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        print(content)
    decoded = json.loads(content)
    print(decoded)


