
"""
from sense_emu import SenseHat

sense = SenseHat()
sense.clear()
# rgb para cor vermalha
r = 255
g = 0
b = 0

print 'Modifique a temperatura e pressao no painel Sense Hat'
print 'Clique em ctrl C para sair'

while True: 
    # obtendo os valores da tela do senseHat
    temp = sense.get_temperature() 
    pressure = sense.get_pressure()

    # verificando se atingiu os valores maximos: 
    # temperatura 40 e pressao 780
    if temp > 40 and pressure > 780:
        sense.clear((r, g, b))
    else:
        sense.clear()
        
"""


"""
from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource

class TempSensor(Resource):
     def __init__(self, name="TempSensor", coap_server=None):
         super(TempSensor, self).__init__(name, coap_server, visible=True,
                                             observable=True, allow_children=True)
         self.payload = "{Temp: 60}"
 
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


class HumiditySensor(Resource):
     def __init__(self, name="HumiditySensor", coap_server=None):
         super(HumiditySensor, self).__init__(name, coap_server, visible=True,
                                             observable=True, allow_children=True)
         self.payload = "{Humidity: 80}"
 
     def render_GET(self, request):
         return self
 
     def render_PUT(self, request):
         self.payload = request.payload
         return self
 
     def render_POST(self, request):
         res = HumiditySensor()
         res.location_query = request.uri_query
         res.payload = request.payload
         return res
 
     def render_DELETE(self, request):
         return True


 class CoAPServer(CoAP):
     def __init__(self, host, port):
         CoAP.__init__(self, (host, port))
         self.add_resource('temp/', TempSensor())
         self.add_resource('humidity/', HumiditySensor())
 
 def main():
     server = CoAPServer("0.0.0.0", 5683)
     try:
         server.listen(10)
     except KeyboardInterrupt:
         print "Server Shutdown"
         server.close()
         print "Exiting..."
 
 if __name__ == '__main__':
     main()
 
"""


from sense_emu import SenseHat
from coapthon.client.helperclient import HelperClient
from coapthon.resources.resource import Resource
from coapthon.server.coap import CoAP
#from threading import Thread
import sys
# autora: Bruna
#   referencias: https://sunnynetwork.wordpress.com/2018/02/15/lab-52/

sense = SenseHat()
sense.clear()

#temp = sense.get_temperature() 
#pressure = sense.get_pressure()

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


class CoAPServer(CoAP):
     def __init__(self, host, port):
         CoAP.__init__(self, (host, port))
         self.add_resource('temp/', TempSensor())
         self.add_resource('pressure/', PressureSensor())
         print self.root.dump()
 
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



"""
class Sensor(Resource):
  def __init__(self,name="Sensor",coap_server=None):
    super(Sensor,self).__init__(name,coap_server,visible=True,observable=True,allow_children=True)
    self.payload = ""
    self.resource_type = "rt1"
    self.content_type = "application/json"
    self.interface_type = "if1"

  def render_GET(self,request):    
    return self

  def render_POST(self, request):
    seres = self.init_resource(request, Sensor())
    return seres

class CoAPServer(CoAP):
  def __init__(self, host, port, multicast=False):
    CoAP.__init__(self,(host,port),multicast)
    self.add_resource('temperature/',Sensor())
    print "CoAP server started on {}:{}".format(str(host),str(port))
    #print self.root.dump()
    print "recurso temperature adicionado"    

def addPressure(server):
    server.add_resource('pressure/', Sensor())
    #print server.root.dump()
    print "recurso pressure adicionado"     

def main():
  ip = sys.argv[1] #localhost
  port = int(sys.argv[2]) #5683
  multicast=False

  server = CoAPServer(ip,port,multicast)
  thread = Thread(target = addPressure, args=(server,))
  thread.setDaemon(True)
  thread.start()

  try:
    server.listen(10)
    print "executed after listen"
  except KeyboardInterrupt:
    print server.root.dump()
    server.close()
    sys.exit()

if __name__=="__main__":
  main()
"""
