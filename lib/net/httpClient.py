import http.client
import json
import ssl
import base64
import mimetypes

class HttpClient():
    def __init__(self):
        self.httpClient = http.client.HTTPSConnection('')

    def tokenRequest(self, options = { 'url', 'path', 'username', 'password' }):
        httpClient = http.client.HTTPSConnection(options['url'], context = ssl._create_unverified_context())
        username = options['username']
        password = options['password']
        authorize = base64.b64encode(f'{username}:{password}'.encode('utf-8'))
        headers = {
            'User-Agent': 'bni-python/0.1.0',
            'Authorization': f'Basic {authorize.decode()}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = 'grant_type=client_credentials'
        
        httpClient.request('POST', options['path'], payload, headers)
        res = httpClient.getresponse()
        data = res.read()
        return json.loads(str(data.decode('utf-8')))

    def request(self, options = { 'method', 'apiKey', 'accessToken', 'url', 'path', 'data' }):
        httpClient = http.client.HTTPSConnection(options['url'], context = ssl._create_unverified_context())
        accessToken = options['accessToken']
        path = options['path']
        url = f'{path}?access_token={accessToken}'
        payload = json.dumps(options['data'])
        headers = {
            'User-Agent': 'bni-python/0.1.0',
            'x-api-key': options['apiKey'],
            'Content-Type': 'application/json'
        }
        httpClient.request(options['method'], url, payload, headers)
        res = httpClient.getresponse()
        data = res.read()
        return json.loads(str(data.decode('utf-8')))