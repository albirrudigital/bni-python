from lib.api.oneGatePayment import OneGatePayment
from lib.util import constants
import unittest
from lib.bniClient import BNIClient


class Test(unittest.TestCase):

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
        data = res['getBalanceResponse']['parameters']['responseCode']
        self.assertEqual(data, '0001')
        print('should return responseCode 0001')

    def testGetInHouseInquiry(self):
        print('\n==============================================')
        one_gate_payment = OneGatePayment(self.client)
        res = one_gate_payment.getInHouseInquiry({
            'accountNo': '115471119'
        })
        self.assertEqual(res['getInHouseInquiryResponse']
                         ['parameters']['responseCode'], '0001')
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
        self.assertEqual(res['doPaymentResponse']
                         ['parameters']['responseCode'], '0001')
        print('should return responseCode 0001')

    def testPaymentStatus(self):
        print('\n==============================================')
        one_gate_payment = OneGatePayment(self.client)
        res = one_gate_payment.getPaymentStatus({
            'customerReferenceNumber': '20170227000000000020',
        })
        self.assertEqual(res['getPaymentStatusResponse']
                         ['parameters']['responseCode'], '0001')
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
        self.assertEqual(res['getInterbankInquiryResponse']
                         ['parameters']['responseCode'], '0001')
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
        self.assertEqual(res['getInterbankPaymentResponse']
                         ['parameters']['responseCode'], '0001')
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
        self.assertEqual(res['holdAmountResponse']
                         ['parameters']['responseCode'], '0001')
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
        self.assertEqual(res['holdAmountReleaseResponse']
                         ['parameters']['responseCode'], '0001')
        print('should return responseCode 0001')


if __name__ == '__main__':
    unittest.main()
