from lib.util import constants
from lib.bniClient import BNIClient
from lib.api.snapBI import SnapBI
import unittest

class TestSnapBI(unittest.TestCase):
    
    client = BNIClient({
            'prod': False,
            'appName': constants.APP_NAME_TEST,
            'clientId': '0bed55cb-c25d-4f07-9c5f-78f7c8aac9da',
            'clientSecret': '46987047-6d56-410d-b43c-abdd247abac2',
            'apiKey': '91ea86f6-387a-49f9-bc55-670e4d2ef67b',
            'apiSecret': 'cc914c89-6b65-475d-a450-58ee4199a1b2',
        })

    def testGetBalance(self):
        print('\n==============================================')
        snap = SnapBI(self.client,  { 'privateKeyPath': 'private.key', 'channelId': '95221' })
        res = snap.balanceInquiry({
            'partnerReferenceNo': '202010290000000000002',
            'accountNo': '0115476117'
        })
        data = res['responseCode']
        self.assertEqual(data, '2000000')
        print('should return responseCode 2000000')

    # def testBankStatement(self):
    #     print('\n==============================================')
    #     snap = SnapBI(self.client,  { 'privateKeyPath': 'private.key', 'channelId': '95221' })
    #     res = snap.bankStatement({
    #         'partnerReferenceNo': '202102102021',
    #         'accountNo': '115233527',
    #         'fromDateTime': '2010-01-01T12:08:56+07:00',
    #         'toDateTime': '2011-01-01T12:08:56+07:00'
    #     })
    #     data = res['responseCode']
    #     self.assertEqual(data, '2001400')
    #     print('should return responseCode 2001400')

    # def testGetInternalAccountInquiry(self):
    #     print('\n==============================================')
    #     snap = SnapBI(self.client,  { 'privateKeyPath': 'private.key', 'channelId': '95221' })
    #     res = snap.internalAccountInquiry({
    #         'partnerReferenceNo': '202010290000000000002',
    #         'beneficiaryAccountNo': '0115476151'
    #     })
    #     data = res['responseCode']
    #     self.assertEqual(data, '2001500')
    #     print('should return responseCode 2001500')

    # def testGetInternalAccountInquiry(self):
        print('\n==============================================')
        snap = SnapBI(self.client,  { 'privateKeyPath': 'private.key', 'channelId': '95221' })
        res = snap.internalAccountInquiry({
            'originalPartnerReferenceNo': '202201911020000121',
            'originalReferenceNo': '220531103343739748',
            'originalExternalId': '20220531103340',
            'serviceCode': '17',
            'transactionDate': '2022-05-31',
            'amount': {
                'value': '15000.00',
                'currency': 'IDR'
                },
            'additionalInfo': {
                'deviceId': '123456',
                'channel': 'mobilephone'
            }
        })
        data = res['responseCode']
        self.assertEqual(data, '2003600')
        print('should return responseCode 2003600')

if __name__ == '__main__':
    unittest.main()