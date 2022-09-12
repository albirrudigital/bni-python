
from bnipython.lib.util import constants
import unittest
from bnipython.lib.bniClient import BNIClient


class TestUtil(unittest.TestCase):
    def testBaseUrl(self):
        print('\n==============================================')
        clientDev = BNIClient(
            {'prod': False, 'clientId': '', 'clientSecret': '', 'apiKey': ''})
        self.assertEqual(clientDev.getBaseUrl(), constants.SANDBOX_BASE_URL)
        print(f'should return {constants.SANDBOX_BASE_URL}')
        clientProd = BNIClient(
            {'prod': True, 'clientId': '', 'clientSecret': '', 'apiKey': ''})
        self.assertEqual(clientProd.getBaseUrl(),
                         constants.PRODUCTION_BASE_URL)
        print(f'should return {constants.PRODUCTION_BASE_URL}')

    def testConfig(self):
        print('\n==============================================')
        client = BNIClient({'prod': False, 'appName': constants.APP_NAME, 'clientId': constants.CLIENT_ID,
                           'clientSecret': constants.CLIENT_SECRET, 'apiKey': constants.API_KEY})
        self.assertEqual(client.getConfig(), {'prod': False, 'appName': constants.APP_NAME,
                         'clientId': constants.CLIENT_ID, 'clientSecret': constants.CLIENT_SECRET, 'apiKey': constants.API_KEY})
        print(
            'should return { prod: false, appName: \'Test APP\', clientId: \'test12345\', clientSecret: \'test54321\', apiKey: \'12345\' }')
