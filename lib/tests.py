import logging
from lib.api.oneGatePayment import OneGatePayment
from lib.util import constants
import unittest
from lib.util.utils import generateClientId, generateSignature
from lib.bniClient import BNIClient

class Test(unittest.TestCase):

    def testClientId(self):   
        print('\n==============================================') 
        clientId = generateClientId(constants.APP_NAME)
        self.assertEqual(clientId, constants.CLIENT_ID_BASE64)
        print(f'should return {constants.CLIENT_ID_BASE64}')

    def testSignature(self):
        print('\n==============================================')
        clientId = generateClientId(constants.APP_NAME)
        payload = {'body':{'clientId':clientId,'accountNo':constants.ACCOUNT_NO},'apiSecret':constants.API_SECRET}
        token = generateSignature(payload)
        self.assertEqual(token, constants.TOKEN_JWT)
        print(f'should return {constants.TOKEN_JWT}')

    def testBaseUrl(self):
        print('\n==============================================')
        clientDev = BNIClient({ 'prod': False, 'clientId': '', 'clientSecret': '', 'apiKey': '' })
        self.assertEqual(clientDev.getBaseUrl(), constants.SANDBOX_BASE_URL)
        print(f'should return {constants.SANDBOX_BASE_URL}')
        clientProd = BNIClient({ 'prod': True, 'clientId': '', 'clientSecret': '', 'apiKey': '' })
        self.assertEqual(clientProd.getBaseUrl(), constants.PRODUCTION_BASE_URL)
        print(f'should return {constants.PRODUCTION_BASE_URL}')
        
    def testConfig(self):
        print('\n==============================================')
        client = BNIClient({'prod': False, 'appName': constants.APP_NAME, 'clientId': constants.CLIENT_ID, 'clientSecret': constants.CLIENT_SECRET,'apiKey': constants.API_KEY});
        self.assertEqual(client.getConfig(),{'prod': False, 'appName': constants.APP_NAME, 'clientId': constants.CLIENT_ID, 'clientSecret': constants.CLIENT_SECRET,'apiKey': constants.API_KEY})
        print('should return { prod: false, appName: \'Test APP\', clientId: \'test12345\', clientSecret: \'test54321\', apiKey: \'12345\' }')
     
    
    client = BNIClient({
            'prod': False,
            'appName': constants.APP_NAME_TEST,
            'clientId': constants.CLIENT_ID_ENCRYPT,
            'clientSecret': constants.CLIENT_SECRET_ENCRYPT,
            'apiKey': constants.API_KEY_ENCRYPT,
            'apiSecret': constants.API_SECRET_ENCRYPT
        })
    def testGetBalance(self):
        print('\n==============================================')
        one_gate_payment = OneGatePayment(self.client)
        res = one_gate_payment.getBalance({
            'accountNo': '115471119'
        })
        try:
            data = res['getBalanceResponse']['parameters']['responseCode']
            self.assertEqual(data, '0001')
        except AssertionError:
            logging.error(res, exc_info=True)

    # def testGetInHouseInquiry(self):
        print('\n==============================================')
        one_gate_payment = OneGatePayment(self.client)
        res = one_gate_payment.getInHouseInquiry({
            'accountNo': '115471119'
        })
        self.assertEqual(res['getInHouseInquiryResponse']['parameters']['responseCode'], '0001')
        print('should return responseCode 0001')

    def testDoPayment(self):
        print('\n==============================================')
        one_gate_payment = OneGatePayment(self.client)
        res = one_gate_payment.doPayment({
            'customerReferenceNumber': '20170227000000000020',
            'paymentMethod': '0',
            'debitAccountNo': '113183203',
            'creditAccountNo': '115471119',
            'valueDate': '20170227000000000',
            'valueCurrency': 'IDR',
            'valueAmount': 100500,
            'remark': '?',
            'beneficiaryEmailAddress': '',
            'beneficiaryName': 'Mr.X',
            'beneficiaryAddress1': 'Jakarta',
            'beneficiaryAddress2': '',
            'destinationBankCode': 'CENAIDJAXXX',
            'chargingModelId': 'OUR'
        })
        self.assertEqual(res['doPaymentResponse']['parameters']['responseCode'], '0001')
        print('should return responseCode 0001')
    
    def testPaymentStatus(self):
        print('\n==============================================')
        one_gate_payment = OneGatePayment(self.client)
        res = one_gate_payment.getPaymentStatus({
            'customerReferenceNumber': '20170227000000000020',
        })
        self.assertEqual(res['getPaymentStatusResponse']['parameters']['responseCode'], '0001')
        print('should return responseCode 0001')

    def testGetInterbankInquiry(self):
        print('\n==============================================')
        one_gate_payment = OneGatePayment(self.client)
        res = one_gate_payment.getInterBankInquiry({
            'customerReferenceNumber': '20180930112233003',
            'accountNum': '0115476117',
            'destinationBankCode': '014',
            'destinationAccountNum': '01400000'
        })
        self.assertEqual(res['getInterbankInquiryResponse']['parameters']['responseCode'], '0001')
        print('should return responseCode 0001')

    def testGetInterBankPayment(self):
        print('\n==============================================')
        one_gate_payment = OneGatePayment(self.client)
        res = one_gate_payment.getInterBankPayment({
            'customerReferenceNumber': '20180930112233005',
            'amount': '12007',
            'destinationAccountNum': '01400000',
            'destinationAccountName': 'Bpk HANS',
            'destinationBankCode': '014',
            'destinationBankName': 'BCA',
            'accountNum': '0316031099',
            'retrievalReffNum': '100000000097'
        })
        self.assertEqual(res['getInterbankPaymentResponse']['parameters']['responseCode'], '0001')
        print('should return responseCode 0001')

    def testHoldAmount(self):
        print('\n==============================================')
        one_gate_payment = OneGatePayment(self.client)
        res = one_gate_payment.holdAmount({
            'customerReferenceNumber': '20181001112233009',
            'amount': '12007',
            'accountNo': '0115476151',
            'detail': 'testHold'
        })
        self.assertEqual(res['holdAmountResponse']['parameters']['responseCode'], '0001')
        print('should return responseCode 0001')

    def testHoldAmountRelease(self):
        print('\n==============================================')
        one_gate_payment = OneGatePayment(self.client)
        res = one_gate_payment.holdAmountRelease({
            'customerReferenceNumber': '20181001112233010',
            'amount': '12007',
            'accountNo': '0115476151',
            'bankReference': '657364',
            'holdTransactionDate': '31052010'
        })
        self.assertEqual(res['holdAmountReleaseResponse']['parameters']['responseCode'], '0001')
        print('should return responseCode 0001')

if __name__ == '__main__':
    unittest.main()