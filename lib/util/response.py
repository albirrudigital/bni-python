def responseOGP(params = { 'res', 'resObj' }):
    if (params['res'][params['resObj']]['parameters']['responseCode']!= '0001'):
        code = params['res'][params['resObj']]['parameters']['responseCode']
        message = params['res'][params['resObj']]['parameters']['responseMessage']
        raise ValueError(f'{code}:{message}')
    else:
        return params['res']

def responseSnapBI(params = { 'res' }):
    statusCodeSuccess = [
        '2000000',
        '2001100',
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
    if not params['res']['responseCode'] in statusCodeSuccess:
        raise ValueError(f"{params['res']['responseCode']} : {params['res']['responseCode']}")
    return params['res']