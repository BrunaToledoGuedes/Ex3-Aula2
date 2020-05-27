#!/usr/bin/env python
import getopt
import socket
import sys
import time

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri

from sense_emu import SenseHat

sense = SenseHat()

red = (255, 0, 0)
white = (255, 255, 255)

t_lim = sys.argv[3]
p_lim = sys.argv[4]
t_path = "coap://"+sys.argv[1]+":"+sys.argv[2]+"/temperature"
p_path = "coap://"+sys.argv[1]+":"+sys.argv[2]+"/pressure"
host, port, path = parse_uri(t_path)
#pixels = [None]*64

# print path
# print host
# print port
# print path
# print h_lim

client = HelperClient(server=(host, port))
responseT = client.post('temperature', t_lim)
#responseP = client.post('pressure', p_lim)
print "response.pretty_print()"
print responseT.pretty_print()
print(t_lim)
#client.stop()

while True:    
    time.sleep(1)
    responseT = client.get(t_lim)
    print("path")
    print(t_path)
    print("response")
    print(responseT)
    temperature = 0
    try:
        temperature = int(responseT.payload)
        print("temperature")
        print(temperature)
        for i in range(64):
            pixels[i] = white
        #if (temperature > h_lim):
            #pixels[led] = red
        sense.set_pixels(pixels)        
    except:
        print('Humidity is not defined or is not a number')


client.stop()
	
