#!/bin/bash

#Iniciando servidor Coap
lxterminal -e sudo python brunaServer_ex3.py &

#Iniciando Atualizador de temperatura e pressao
lxterminal -e sudo python brunaUpdateServer_ex3.py &

#Iniciando um programa cliente de exemplo
#  passando 40 de temperatura e 600 de pressao como parametros
lxterminal -e sudo python brunaClient_ex3.py -t 40 -p 600
