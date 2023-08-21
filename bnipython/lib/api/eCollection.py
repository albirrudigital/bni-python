from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util.utils import generateClientId, generateSignature
from bnipython.lib.util.response import responseOGP


class eCollection():
    def __init__(self, client):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()
        self.httpClient = HttpClient()