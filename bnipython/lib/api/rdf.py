from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateUUID, generateSignature, getTimestamp
from bnipython.lib.util.response import responseRDF

class RDF():
    def __init__(self, client):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()
        self.httpClient = HttpClient()
    
    def inquiryAccountBalance(self, params={
        'companyId', 
        'parentCompanyId', 
        'requestUuid',
        'accountNumber'
    }):
        timeStamp = getTimestamp()
        payload = {}
        payload['request'] = {}
        payload['request'] = {
            'header': {
                'companyId': params['companyId'],
                'parentCompanyId': params['parentCompanyId'],
                'requestUuid': generateUUID()
            },
            'accountNumber': params['accountNumber']
        }
        payload = {**payload, **{ 'timestamp': timeStamp}}
        signature = generateSignature(
            {'body': payload, 'apiSecret': self.client['apiSecret']}
        )
        res = self.httpClient.requestV2({
            'method': 'POST',
            'apiKey': self.client['apiKey'],
            'accessToken': self.token,
            'url': f'{self.baseUrl}',
            'path': '/rdf/v2.1/inquiry/account/balance',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload
        })
        return responseRDF(params={'res': res})
    
    def inquiryAccountInfo(self, params={
        'companyId', 
        'parentCompanyId', 
        'requestUuid',
        'accountNumber'
    }):
        timeStamp = getTimestamp()
        payload = {}
        payload['request'] = {}
        payload['request'] = {
            'header': {
                'companyId': params['companyId'],
                'parentCompanyId': params['parentCompanyId'],
                'requestUuid': generateUUID()
            },
            'accountNumber': params['accountNumber']
        }
        payload = {**payload, **{ 'timestamp': timeStamp}}
        signature = generateSignature(
            {'body': payload, 'apiSecret': self.client['apiSecret']}
        )
        res = self.httpClient.requestV2({
            'method': 'POST',
            'apiKey': self.client['apiKey'],
            'accessToken': self.token,
            'url': f'{self.baseUrl}',
            'path': '/rdf/v2.1/inquiry/account/info',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload
        })
        return responseRDF(params={'res': res})

    def paymentUsingTransfer(self, params={
        'companyId', 
        'parentCompanyId', 
        'requestUuid',
        'accountNumber',
        'accountNumber',
        'beneficiaryAccountNumber',
        'currency',
        'amount',
        'remark'
    }):
        timeStamp = getTimestamp()
        payload = {}
        payload['request'] = {
            'header': { 
                'companyId': 'SANDBOX', 
                'parentCompanyId': 'STI_CHS', 
                'requestUuid': generateUUID() 
            }, 
            'accountNumber': '0115476117', 
            'beneficiaryAccountNumber': '0115471119', 
            'currency': 'IDR', 
            'amount': '11500', 
            'remark': 'Test P2PL'
        }
        payload = {**payload, **{ 'timestamp': timeStamp}}
        signature = generateSignature(
            {'body': payload, 'apiSecret': self.client['apiSecret']}
        )
        res = self.httpClient.requestV2({
            'method': 'POST',
            'apiKey': self.client['apiKey'],
            'accessToken': self.token,
            'url': f'{self.baseUrl}',
            'path': '/rdf/v2.1/payment/transfer',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload
        })
        return responseRDF(params={'res': res})


    