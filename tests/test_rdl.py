from bnipython.lib.api.rdl import RDL
from bnipython.lib.util import constants
import unittest
from bnipython.lib.bniClient import BNIClient

class TestRDL(unittest.TestCase):
    client = BNIClient({
        'env': 'sandbox-dev',
        'appName': constants.APP_NAME,
        'clientId': constants.CLIENT_ID_ENCRYPT,
        'clientSecret': constants.CLIENT_SECRET_ENCRYPT,
        'apiKey': constants.API_KEY_ENCRYPT,
        'apiSecret': constants.API_SECRET_ENCRYPT
    })

    def testRegisterInvestor(self):
        print('\n==============================================')
        rekening_dana_nasabah = RDL(self.client)
        res = rekening_dana_nasabah.registerInvestor({
            'companyId': 'SANDBOX',
            'parentCompanyId': 'STI_CHS',
            'uuidFaceRecog': '40FCB72E71D35C81',
            'title': '01',
            'firstName': 'Agus',
            'middleName': '',
            'lastName': 'Saputra',
            'optNPWP': '1',
            'npwpNum': '001058893408123',
            'nationality': 'ID',
            'domicileCountry': 'ID',
            'religion': '2',
            'birthPlace': 'Semarang',
            'birthDate': '14081982',
            'gender': 'M',
            'isMarried': 'S',
            'motherMaidenName': 'Dina Maryti',
            'jobCode': '01',
            'education': '07',
            'idType': '01',
            'idNumber': '4147016201959998',
            'idIssuingCity': 'Jakarta Barat',
            'idExpiryDate': '26102099',
            'addressStreet': 'Jalan Mawar Melati',
            'addressRtRwPerum': '003009Sentosa',
            'addressKel': 'Cengkareng Barat',
            'addressKec': 'Cengkareng/Jakarta Barat',
            'zipCode': '11730',
            'homePhone1': '0214',
            'homePhone2': '7459',
            'officePhone1': '',
            'officePhone2': '',
            'mobilePhone1': '0812',
            'mobilePhone2': '12348331',
            'faxNum1': '',
            'faxNum2': '',
            'email': 'agus.saputra@gmail.com',
            'monthlyIncome': '8000000',
            'branchOpening': '0259',
            'employerName': 'Salman',
            'employerAddDet': 'St Baker',
            'employerAddCity': 'Arrandelle',
            'jobDesc': '13',
        })
        data = res['response']['responseCode']
        self.assertEqual(data, '0001')
        print('\033[92m should return responseCode 0001 \033[0m')