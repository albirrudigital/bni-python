from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateUUID, generateSignature, getTimestamp
from bnipython.lib.util.response import responseRDL

class RDL():
    def __init__(self, client):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()
        self.httpClient = HttpClient()

    def faceRecognition(self, params={
        'companyId',
        'parentCompanyId',
        'requestUuid',
        'firstName',
        'middleName',
        'lastName',
        'idNumber',
        'birthDate',
        'birthPlace',
        'gender',
        'cityAddress',
        'stateProcAddress',
        'addressCountry',
        'streetAddress1',
        'streetAddress2',
        'postAddress',
        'country',
        'selfiePhoto'
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
            'firstName': params['firstName'],
            'middleName': params['middleName'],
            'lastName': params['lastName'],
            'idNumber': params['idNumber'], 
            'birthDate': params['birthDate'], 
            'birthPlace': params['birthPlace'], 
            'birthDate': params['birthDate'],
            'birthPlace': params['birthPlace'],
            'gender': params['gender'],
            'cityAddress': params['cityAddress'],
            'stateProvAddress': params['stateProvAddress'],
            'addressCountry': params['addressCountry'],
            'streetAddress1': params['streetAddress1'],
            'streetAddress2': params['streetAddress2'],
            'postCodeAddress': params['postCodeAddress'],
            'country': params['country'],
            'selfiePhoto': params['selfiePhoto']
        }
        payload = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payload, 'apiSecret': self.client['apiSecret']})
        res = self.httpClient.requestV2({
            'method': 'POST',
            'apiKey': self.client['apiKey'],
            'accessToken': self.token,
            'url': f'{self.baseUrl}',
            'path': '/rekdana/v1.1/face/recog',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': {'request': payload['request']}
        })
        return responseRDL(params={'res': res, 'resObj': 'faceRecognitionResponse'})
        

    def registerInvestor(self, params={
        'companyId',
        'parenCompanyId',
        'uuidFaceRecog',
        'title',
        'firstName',
        'middleName',
        'lastName',
        'optNPWP',
        'npwpNum',
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
        'idType',
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
            'npwpNum': params['npwpNum'],
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
            'idType': params['idType'],
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
            'mobilePhone1': params['mobilePhone1'],
            'mobilePhone2': params['mobilePhone2'],
            'faxNum1': params['faxNum1'],
            'faxNum2': params['faxNum2'],
            'branchOpening': params['branchOpening'],
            'monthlyIncome': params['monthlyIncome'],
            'email': params['email'],
            'employerName': params['employerName'],
            'employerAddDet': params['employerAddDet'],
            'employerAddCity': params['employerAddCity'],
            'jobDesc': params['jobDesc'],
        }
        payload = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payload, 'apiSecret': self.client['apiSecret']})
        res = self.httpClient.requestV2({
            'method': 'POST',
            'apiKey': self.client['apiKey'],
            'accessToken': self.token,
            'url': f'{self.baseUrl}',
            'path': '/p2pl/v2.1/register/investor',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': {'request': payload['request']}
        })
        return responseRDL(params={'res': res, 'resObj': 'registerInvestorResponse'})