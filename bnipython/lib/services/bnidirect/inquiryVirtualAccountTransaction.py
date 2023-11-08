from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateSignature, getTimestamp
from bnipython.lib.util.response import responseBniDirect

def inquiryVirtualAccountTransaction(params):
        httpClient = HttpClient();
        timeStamp = getTimestamp()
        payload = {
                'corporateId': params['body']['corporateId'],
                'userId': params['body']['userId'],
                'virtualAccountNo': params['body']['virtualAccountNo'],
                'fromDate': params['body']['fromDate'],
                'toDate': params['body']['toDate'],
        }
        payloadSignature = {**payload, **{ 'timestamp': timeStamp }}
        signature = generateSignature(
            {'body': payloadSignature, 'apiSecret': params['config']['client']['apiSecret']})
        res = httpClient.requestV2BniDirect({
            'method': 'POST',
            'apiKey': params['config']['client']['apiKey'],
            'accessToken': params['config']['token'],
            'url': f'{params['config']['baseUrl']}',
            'path': '/bnidirect/api/VirtualAccount/InquiryTransaction',
            'signature': signature.split('.')[2],
            'timestamp': timeStamp,
            'data': payload,
            'bniDirectKey': 'dc8f7943e027345677c7dade0441936c3bb3f8d697ef8f7b28ae5dfdeea78dd1'
        })
        return responseBniDirect(params={'res': res})