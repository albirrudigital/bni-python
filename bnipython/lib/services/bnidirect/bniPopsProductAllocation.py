from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp
from bnipython.lib.util.response import responseBniDirect

def bniPopsProductAllocation(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'corporateId': params['body']['corporateId'],
                'userId': params['body']['userId'],
                'debitAccountNo': params['body']['debitAccountNo'],
                'salesOrganizationCode': params['body']['salesOrganizationCode'],
                'distributionChannelCode': params['body']['distributionChannelCode'],
                'productCode': params['body']['productCode'],
                'shipTo': params['body']['shipTo'],
                'scheduleAggreementNo': params['body']['scheduleAggreementNo'],
                'debitOrCreditNoteNo': params['body']['debitOrCreditNoteNo'],
                'productInformationDetail': params['body']['productInformationDetail'],
        }
        payloadSignature = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payloadSignature, 'apiSecret': params['config']['client']['apiSecret']})
        res = httpClient.requestV2BniDirect({
            'method': 'POST',
            'apiKey': params['config']['client']['apiKey'],
            'accessToken': params['config']['token'],
            'url': f'{params['config']['baseUrl']}',
            'path': '/bnidirect/api/BNIPOPS/ProductAllocation/Payment',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': 'dc8f7943e027345677c7dade0441936c3bb3f8d697ef8f7b28ae5dfdeea78dd1'
        })
        return responseBniDirect(params={'res': res})