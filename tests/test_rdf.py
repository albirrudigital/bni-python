from bnipython.lib.api.rdf import RDF
from bnipython.lib.util import constants
import unittest
from bnipython.lib.bniClient import BNIClient
import json

class TestRDF(unittest.TestCase):
    client = BNIClient({
        'env': 'sandbox-dev',
        # 'appName': constants.APP_NAME,
        'clientId': constants.CLIENT_ID_ENCRYPT,
        'clientSecret': constants.CLIENT_SECRET_ENCRYPT,
        'apiKey': constants.API_KEY_ENCRYPT,
        'apiSecret': constants.API_SECRET_ENCRYPT
    })

    def testInquiryAccountBalance(self):
        print('\n============================================')
        rekening_dana_funder = RDF(self.client)
        res = rekening_dana_funder.inquiryAccountBalance({
            'companyId': 'SANDBOX', 
            'parentCompanyId': 'STI_CHS', 
            'requestUuid': 'E26DB4C8F6484E72', 
            'accountNumber': '0115476117'
        })
        data = res['response']['responseCode']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0001')
        print('should return responseCode 0001')
        
    def testInquiryAccountInfo(self):
        print('\n============================================')
        rekening_dana_funder = RDF(self.client)
        res = rekening_dana_funder.inquiryAccountInfo({
            'companyId': 'SANDBOX', 
            'parentCompanyId': 'STI_CHS', 
            'requestUuid': 'E26DB4C8F6484E72', 
            'accountNumber': '0115476117'
        })
        data = res['response']['responseCode']
        # print(json.dumps(res, indent=2))
        self.assertEqual(data, '0001')
        print('should return responseCode 0001')

    def testPaymentUsingTransfer(self):
        print('\n============================================')
        rekening_dana_funder = RDF(self.client)
        res = rekening_dana_funder.paymentUsingTransfer({
            'companyId': 'SANDBOX', 
            'parentCompanyId': 'STI_CHS', 
            'requestUuid': 'E8C6E0027F6E429F', 
            'accountNumber': '0115476117', 
            'beneficiaryAccountNumber': '0115471119', 
            'currency': 'IDR', 
            'amount': '11500', 
            'remark': 'Test P2PL'
        })
        data = res['response']['responseCode']
        self.assertEqual(data, '0001')
        print('should return responseCode 0001')