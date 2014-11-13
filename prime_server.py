__author__ = 'Greg Richards'

import rpyc
from rpyc.utils.server import ThreadedServer

from primenumbers import *


class Prime_Service(rpyc.Service):

    def on_connect(self):
        pass
        #created a connection

    def on_disconnect(self):
        pass
        #connection is closed

    def exposed_get_primes(self, number):
        return Prime.get_primes(Prime, number)



if__name__=="__main__":
    server = ThreadedServer(Prime_Service, port = 54321)
    server.start()
    #start up the server