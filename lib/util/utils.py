import base64
import hmac
import hashlib
import json

def generateSignature(params):
    # generate JWT header
    header = escape(base64.b64encode('{"alg":"HS256","typ":"JWT"}'.encode('utf-8')).decode())
    # generate JWT payload
    # print(json.dumps(params['body'],separators=(',', ':')))
    payload = escape(base64.b64encode(json.dumps(params['body'],separators=(',', ':')).encode('utf-8')).decode())
    encript = header+'.'+payload
    # generate JWT signature
    jwtSignature = escape(base64.b64encode(hmac.new(str(params['apiSecret']).encode('utf-8'),
                        encript.encode('utf-8'), hashlib.sha256).digest()).decode())
    return f"{header}.{payload}.{jwtSignature}"  

def generateClientId(appName):
    clientId = base64.b64encode(appName.encode('utf-8'))
    return f"IDBNI{clientId.decode()}"

def escape(string):
    return string.replace('+','-').replace('/','_').replace('=','')