from sense_emu import SenseHat
from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri
import argparse

sense = SenseHat()
sense.clear()
# rgb para cor vermalha
r = 255
g = 0
b = 0

# Prepare for cmd line arguments
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-t", "--temp", help="Valor limite para temperatura", default=40)
parser.add_argument("-p", "--pres", help="Valor limite para Pressao", default=600)
args = parser.parse_args()

tlim = float(args.temp)
plim = float(args.pres)
tempx = 0
pressurex = 0

print 'Modifique a temperatura e pressao no painel Sense HAT'
print 'Clique em ctrl C para sair'

global client
client = HelperClient(server=('127.0.0.1', 5683))
while True: 
    # obtendo os valores do servidor COAP
    responseT = client.get('temp')
    #print 'temperatura: ',responseT.payload   # .pretty_print()
    responseP = client.get('pressure')
    #print 'Pressao: ', responseP.payload

    temp = float(responseT.payload)  #  sense.get_temperature() 
    pressure = float(responseP.payload)   #  sense.get_pressure()
    if temp+pressure != tempx+pressurex:
       print "======================================"
       print "Temperatura e Pressao maxima permitida"
       print tlim, plim
       print "Temperatura e Pressao atual"
       print temp, pressure
       tempx = temp
       pressurex = pressure
    # verificando se atingiu os valores maximos: 
    # temperatura tlim e pressao plim
    if temp > tlim and pressure > plim:
        sense.clear((r, g, b))
    else:
        sense.clear()
