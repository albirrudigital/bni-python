from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateUUID, generateSignature, getTimestamp

class RDN():
    def __init__(self, client):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()
        self.httpClient = HttpClient()

    def registerInvestor(self, params={
        'companyId',
        'parenCompanyId',
        'uuidFaceRecog',
        'title',
        'firstName',
        'middleName',
        'lastName',
        'optNPWP',
        'nationality',
        'domicileCountry',
        'religion',
        'birthPlace',
        'birthDate',
        'gender',
        'isMarried',
        'motherMaidenName',
        'jobCode',
        'education',
        'idNumber',
        'idIssuingCity',
        'idExpiryDate',
        'addressStreet',
        'addressRtRwPerum',
        'addressKel',
        'addressKec',
        'zipCode',
        'homePhone1',
        'homePhone2',
        'officePhone1',
        'officePhone2',
        'faxNum1',
        'faxNum2',
        'email',
        'monthlyIncome',
        'branchOpening',
        'institutionName',
        'sid',
        'employerName',
        'employerAddDet',
        'employerAddCity',
        'jobDesc',
        'ownedBankAccNo',
        'idIssuingDate'
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
            'uuidFaceRecog': params['uuidFaceRecog'],
            'title': params['title'],
            'firstName': params['firstName'],
            'middleName': params['middleName'],
            'lastName': params['lastName'],
            'optNPWP': params['optNPWP'],
            'nationality': params['nationality'],
            'domicileCountry': params['domicileCountry'],
            'religion': params['religion'],
            'birthPlace': params['birthPlace'],
            'birthDate': params['birthDate'],
            'gender': params['gender'],
            'isMarried': params['isMarried'],
            'motherMaidenName': params['motherMaidenName'],
            'jobCode': params['jobCode'],
            'education': params['education'],
            'idNumber': params['idNumber'],
            'idIssuingCity': params['idIssuingCity'],
            'idExpiryDate': params['idExpiryDate'],
            'idExpiryDate': params['addressStreet'],
            'addressRtRwPerum': params['addressRtRwPerum'],
            'addressKel': params['addressKel'],
            'addressKec': params['addressKec'],
            'zipCode': params['zipCode'],
            'homePhone1': params['homePhone1'],
            'homePhone2': params['homePhone2'],
            'officePhone1': params['officePhone1'],
            'officePhone2': params['officePhone2'],
            'faxNum1': params['faxNum1'],
            'faxNum2': params['faxNum2'],
            'email': params['email'],
            'monthlyIncome': params['monthlyIncome'],
            'branchOpening': params['branchOpening'],
            'institutionName': params['institutionName'],
            'sid': params['sid'],
            'employerName': params['employerName'],
            'employerAddDet': params['employerAddDet'],
            'employerAddCity': params['employerAddCity'],
            'jobDesc': params['jobDesc'],
            'ownedBankAccNo': params['ownedBankAccNo'],
            'idIssuingDate': params['idIssuingDate']
        }
        payload = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payload, 'apiSecret': self.client['apiSecret']})
        res = self.httpClient.requestV2({
            'method': 'POST',
            'apiKey': self.client['apiKey'],
            'accessToken': self.token,
            'url': f'{self.baseUrl}',
            'path': '/rdn/v2.1/register/investor',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload
        })
        return res