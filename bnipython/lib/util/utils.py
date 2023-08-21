import base64
import hmac
import hashlib
import json
import pytz
import random
import math
import string
import random
import time
from OpenSSL import crypto
from datetime import datetime

def generateSignature(params):
    # generate JWT header
    header = escape(base64.b64encode(
        '{"alg":"HS256","typ":"JWT"}'.encode('utf-8')).decode())
    # generate JWT payload
    payload = escape(base64.b64encode(json.dumps(
        params['body'], separators=(',', ':')).encode('utf-8')).decode())
    encript = header+'.'+payload
    # generate JWT signature
    jwtSignature = escape(base64.b64encode(hmac.new(str(params['apiSecret']).encode('utf-8'),
                                                    encript.encode('utf-8'), hashlib.sha256).digest()).decode())
    return f"{header}.{payload}.{jwtSignature}"


def generateClientId(appName):
    clientId = base64.b64encode(appName.encode('utf-8'))
    return f"IDBNI{clientId.decode()}"


def escape(string):
    return string.replace('+', '-').replace('/', '_').replace('=', '')

def getTimestamp():
    return datetime.now(pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%dT%H:%M:%S+07:00')


def generateTokenSignature(params={'privateKeyPath', 'clientId', 'timeStamp'}):
    privateKeyPath = params['privateKeyPath']
    rsaPrivate = privateKeyPath.replace('./', '')
    keyFile = open(f'{rsaPrivate}', 'rb')
    key = keyFile.read()
    keyFile.close()

    pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)
    clienId = params['clientId']
    times = params['timeStamp']
    data = f"{clienId}|{times}"

    dataBytes = bytes(data, encoding='utf-8')
    signature = base64.b64encode(crypto.sign(pkey, dataBytes, "sha256"))
    return signature.decode()


def generateSignatureServiceSnapBI(params={'body', 'method', 'url', 'accessToken', 'timeStamp', 'apiSecret'}):
    minify = json.dumps(params['body'], separators=(',', ':'))
    shaHex = hashlib.sha256(minify.encode('utf-8')).hexdigest()
    lower = shaHex.lower()

    stringToSign = f"{params['method']}:{params['url']}:{params['accessToken']}:{lower}:{params['timeStamp']}"

    gen_hmac = hmac.new(str(params['apiSecret']).encode(
        'utf-8'), stringToSign.encode('utf-8'), hashlib.sha512)
    data = base64.b64encode(gen_hmac.digest())
    return data.decode()


def randomNumber():
    randomNumber = random.randint(100000000, 999999999)
    unixTimeStamp = math.floor(datetime.timestamp((datetime.now())))
    return f'{randomNumber}{unixTimeStamp}'

def generateUUID(length=16):
    characters = string.ascii_uppercase + string.digits
    uuid = ''.join(random.choice(characters) for _ in range(length))
    return uuid

TIME_DIFF_LIMIT = 480

def encrypt(json_data, cid, secret):
    t = str(int(time.time()))[::-1]
    return doubleEncrypt(t + "." + json.dumps(json_data), cid, secret)

def decrypt(hased_string, cid, secret):
    parseStr = doubleDecrypt(hased_string, cid, secret)
    data = parseStr.split(".", 1)
    if len(data) == 2:
        strrevtime = data[0][::-1]
        if tsDiff(int(strrevtime)):
            return data[1]
    return None

def tsDiff(ts):
    return math.fabs(ts - time.time()) <= TIME_DIFF_LIMIT

def doubleEncrypt(stringObj, cid, secret):
    result = ''
    result = enc(stringObj, cid)
    result = enc(result, secret)
    # result = result.encode('base64')
    # result = base64.b64encode(result)
    result = base64.b64encode(bytes(result, 'utf-8'))
    result = str(result, "utf-8")
    result = result.rstrip('=')
    # result = result.replace(b'=',b'')
    result = result.translate(str.maketrans('+/', '-_'))
    # result = result.replace(b'+/',b'-_')
    return result

def enc(string, key):
    result = ""
    strls = len(string)
    strlk = len(key)
    for i in range(0, strls):
        char = string[i:i+1]
        st = (i % strlk) - 1
        xlen = None if st < 0 else st+1
        keychar = key[st:xlen]
        char = chr((ord(char) + ord(keychar)) % 128)
        result += char

    return result

def doubleDecrypt(string, cid, secret):
    ceils = math.ceil(len(string) / 4.0) * 4
    while (len(string) < ceils):
        string += "="

    string = string.replace('-', '+').replace('_', '/')
    result = base64.b64decode(bytes(string, 'utf-8'))
    # result = string.decode('base64')
    result = dec(result, cid)
    result = dec(result, secret)
    return result

@staticmethod
def dec(string, key):
    result = ''
    strls = len(string)
    strlk = len(key)
    for i in range(0, strls):
        char = string[i:i+1]
        st = (i % strlk) - 1
        xlen = None if st < 0 else st+1
        keychar = key[st:xlen]
        char = chr((ord(char) - ord(keychar) + 256) % 128)
        result += char

    return result