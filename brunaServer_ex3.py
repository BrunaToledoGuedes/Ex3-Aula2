from sense_emu import SenseHat
from coapthon.client.helperclient import HelperClient
from coapthon.resources.resource import Resource
from coapthon.server.coap import CoAP
import sys
# autora: Bruna
#   referencias: https://sunnynetwork.wordpress.com/2018/02/15/lab-52/

sense = SenseHat()
sense.clear()

# Armazena o valor do sensor de temperatura
class TempSensor(Resource):
     def __init__(self, name="TempSensor", coap_server=None):
         super(TempSensor, self).__init__(name, coap_server, visible=True,
                                             observable=True, allow_children=True)
         temp = sense.get_temperature() 
         self.payload = str(temp)  #"{Temp: 0}"
 
     def render_GET(self, request):
         return self
 
     def render_PUT(self, request):
         self.payload = request.payload
         return self
 
     def render_POST(self, request):
         res = TempSensor()
         res.location_query = request.uri_query
         res.payload = request.payload
         return res
 
     def render_DELETE(self, request):
         return True

# Armazena o valor do sensor de pressão
class PressureSensor(Resource):
     def __init__(self, name="PressureSensor", coap_server=None):
         super(PressureSensor, self).__init__(name, coap_server, visible=True,
                                             observable=True, allow_children=True)
         pressure = sense.get_pressure()
         self.payload = str(pressure)  #"{Pressure: 0}"
 
     def render_GET(self, request):
         return self
 
     def render_PUT(self, request):
         self.payload = request.payload
         return self
 
     def render_POST(self, request):
         res = PressureSensor()
         res.location_query = request.uri_query
         res.payload = request.payload
         return res
 
     def render_DELETE(self, request):
         return True

# Servidor COAP
class CoAPServer(CoAP):
     def __init__(self, host, port):
         CoAP.__init__(self, (host, port))
         self.add_resource('temp/', TempSensor())
         self.add_resource('pressure/', PressureSensor())
         print self.root.dump()

# Iniciando Serviço
def main():
     server = CoAPServer("127.0.0.1", 5683)
     try:
         while True:
             server.listen()
             print "escutando"
     except KeyboardInterrupt:
         print "Server Shutdown"
         server.close()
         print "Exiting..."
 
if __name__ == '__main__':
     main()
