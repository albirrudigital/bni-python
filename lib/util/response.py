def responseSnapBI(params = { 'res' }):
    statusCodeSuccess = [
        '2000000',
        '2001400',
        '2001500',
        '2001600',
        '2001700',
        '2001800',
        '2002200',
        '2002300',
        '2003600',
        '2007300'
    ]
    print(params)
    if params['responseCode'] in statusCodeSuccess:
        return f"{params['responseCode']} : {params['res']['responseCode']}"
    return params['res']

def responseOGPGetBalance(params = { 'res' }):
    
    if (params['getBalanceResponse']['parameters']['responseCode'] != '0001'):
        return f"{params['res']['getBalanceResponse']['parameters']['responseCode']} : {['params']['res']['getBalanceResponse']['parameters']['responseMessage']}"
    else:
        return params['res']