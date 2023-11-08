from bnipython.lib.services.bnidirect import bulkGetStatus
from bnipython.lib.services.bnidirect import bniPopsCashAndCarry
from bnipython.lib.services.bnidirect import bniPopsProductAllocation
from bnipython.lib.services.bnidirect import bniPopsResubmitCashAndCarry
from bnipython.lib.services.bnidirect import bniPopsResubmitProductAllocation
from bnipython.lib.services.bnidirect import inquiryVirtualAccountTransaction
from bnipython.lib.services.bnidirect import updateVirtualAccount
from bnipython.lib.services.bnidirect import createVirtualAccount

class BNIDIRECT():
     def __init__(self, client):
        self.client = client.config
        self.baseUrl = client.getBaseUrl()
        self.config = client.getConfig()
        self.token = client.getToken()

     def bulkGetStatus(self, params):
         res = bulkGetStatus.bulkGetStatus({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def bniPopsCashAndCarry(self, params):
         res = bniPopsCashAndCarry.bniPopsCashAndCarry({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def bniPopsProductAllocation(self, params):
         res = bniPopsProductAllocation.bniPopsProductAllocation({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def bniPopsResubmitCashAndCarry(self, params):
         res = bniPopsResubmitCashAndCarry.bniPopsResubmitCashAndCarry({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def bniPopsResubmitProductAllocation(self, params):
         res = bniPopsResubmitProductAllocation.bniPopsResubmitProductAllocation({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def inquiryVirtualAccountTransaction(self, params):
         res = inquiryVirtualAccountTransaction.inquiryVirtualAccountTransaction({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def updateVirtualAccount(self, params):
         res = updateVirtualAccount.updateVirtualAccount({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res
     
     def createVirtualAccount(self, params):
         res = createVirtualAccount.createVirtualAccount({
             'body': params,
             'config': {
                 'client': self.client,
                 'baseUrl': self.baseUrl,
                 'config': self.config,
                 'token': self.token
             }
         })
         return res