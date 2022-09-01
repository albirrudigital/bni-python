from lib.net.httpClient import HttpClient
from lib.util.utils import generateClientId, generateSignature

class OneGatePayment():
    def __init__(self, client):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()
        self.httpClient = HttpClient()

    def getBalance(self, params = { 'accountNo' }):
        payload = {}
        body = {
            'accountNo': params['accountNo'],
            'clientId': generateClientId(self.client['appName'])
        }
        payload = body
        payload['signature'] = generateSignature({ 'body': body, 'apiSecret': self.client['apiSecret'] })
        
        res = self.httpClient.request({
                'method': 'POST',
                'apiKey': self.client['apiKey'],
                'accessToken': self.token,
                'url': f'{self.baseUrl}',
                'path': '/H2H/v2/getbalance',
                'data': payload
                })
        return res

    def getInHouseInquiry(self, params = { 'accountNo' }):
        payload = {}
        body = {
            'accountNo': params['accountNo'],
            'clientId': generateClientId(self.client['appName'])
        }
        payload = body
        payload['signature'] = generateSignature({ 'body': body, 'apiSecret': self.client['apiSecret'] })

        res = self.httpClient.request({
                'method': 'POST',
                'apiKey': self.client['apiKey'],
                'accessToken': self.token,
                'url': f'{self.baseUrl}',
                'path': '/H2H/v2/getinhouseinquiry',
                'data': payload
            })
        return res

    def doPayment(self,
        params = {
            'customerReferenceNumber',
            'paymentMethod',
            'debitAccountNo',
            'creditAccountNo',
            'valueDate',
            'valueCurrency',
            'valueAmount',
            'remark',
            'beneficiaryEmailAddress',
            'beneficiaryName',
            'beneficiaryAddress1',
            'beneficiaryAddress2',
            'destinationBankCode',
            'chargingModelId'
        }):
        payload = {}
        body = {
            'clientId': generateClientId(self.client['appName']),
            'customerReferenceNumber': params['customerReferenceNumber'],
            'paymentMethod': params['paymentMethod'],
            'debitAccountNo': params['debitAccountNo'],
            'creditAccountNo': params['creditAccountNo'],
            'valueDate': params['valueDate'],
            'valueCurrency': params['valueCurrency'],
            'valueAmount': params['valueAmount'],
            'remark': params['remark'],
            'beneficiaryEmailAddress': params['beneficiaryEmailAddress'],
            'beneficiaryName': params['beneficiaryName'],
            'beneficiaryAddress1': params['beneficiaryAddress1'],
            'beneficiaryAddress2': params['beneficiaryAddress2'],
            'destinationBankCode': params['destinationBankCode'],
            'chargingModelId': params['chargingModelId']
        }

        payload = body
        payload['signature'] = generateSignature({ 'body': body, 'apiSecret': self.client['apiSecret'] })

        res = self.httpClient.request({
                    'method': 'POST',
                    'apiKey': self.client['apiKey'],
                    'accessToken': self.token,
                    'url': f'{self.baseUrl}',
                    'path': '/H2H/v2/dopayment',
                    'data': payload
                })
        return res

    def getPaymentStatus(self, params = { 'customerReferenceNumber' }):
        payload = {}
        body = {
            'clientId': generateClientId(self.client['appName']),
            'customerReferenceNumber': params['customerReferenceNumber']
        }

        payload = body
        payload['signature'] = generateSignature({ 'body': body, 'apiSecret': self.client['apiSecret'] })
        res = self.httpClient.request({
                    'method': 'POST',
                    'apiKey': self.client['apiKey'],
                    'accessToken': self.token,
                    'url': f'{self.baseUrl}',
                    'path': '/H2H/v2/getpaymentstatus',
                    'data': payload
                })
        
        return res