from bnipython.lib.api.eCollection import eCollection
from bnipython.lib.util import constants
import unittest
from bnipython.lib.bniClient import BNIClient


class TestUtil(unittest.TestCase):
    client = BNIClient({
        'env': 'sandbox',
        'appName': constants.APP_NAME,
        'clientId': constants.CLIENT_ID_ENCRYPT,
        'clientSecret': constants.CLIENT_SECRET_ENCRYPT,
        'apiKey': constants.API_KEY_ENCRYPT,
        'apiSecret': constants.API_SECRET_ENCRYPT
    })

    def testInvoiceBilling(self):
        print('\n==============================================')
        e_collection = eCollection(self.client)
        res = e_collection.getBalance({
            'client_id' : '001',
            'trx_amount' : '100000',
            'customer_name' : 'Mr. X',
            'customer_email' : 'xxx@email.com', 
            'customer_phone' : '08123123123', 
            'virtual_account' : '8001000000000001', 
            'trx_id' : '1230000001',
            'datetime_expired' : '2015-07-01 16:00:00', 
            'description' : 'Payment of transaction ABC', 
            'type' : 'createBilling'
        })
        print(res)
        data = res['getBalanceResponse']['parameters']['responseCode']
        self.assertEqual(data, '0001')
        print('should return responseCode 0001')
