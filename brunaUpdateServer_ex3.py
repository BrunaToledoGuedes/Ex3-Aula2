#!/usr/bin/env python
import getopt
import socket
import sys
import time
from sense_emu import SenseHat
from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri

sense = SenseHat()
sense.clear()

# Autora Bruna
# Atualiza a variavel payload do servidor coap com a temperatura e pressao obtidas pelo SenseHat

client = None

def main(): 
    global client

    client = HelperClient(server=('127.0.0.1', 5683))
    try:
         while True:
            time.sleep(5)            
            responseT = client.put('temp', str(sense.get_temperature())) 
            responseP = client.put('pressure', str(sense.get_pressure())) 
            response = client.get('temp')
            print response.pretty_print()
            response = client.get('pressure')
            print response.pretty_print()
            #print responseT.pretty_print()
    except KeyboardInterrupt:
         print "Server Shutdown"
         server.close()
         print "Exiting..."

if __name__ == '__main__': 
    main()
