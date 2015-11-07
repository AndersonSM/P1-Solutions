# coding: utf-8
import math

primeira_vez = True
soma_dist = 0
num_tiros = 0
melhor_tiro = 0

while True:
    x = float(raw_input())
    y = float(raw_input())
    distancia = math.sqrt((x**2) + (y**2))
    if distancia > 200: break
    
    if primeira_vez == True:
        primeira_vez = False
        melhor_tiro = distancia
    
    soma_dist += distancia
    num_tiros += 1
    
    if distancia <= melhor_tiro:
        melhor_tiro = distancia
        print "%.2f cm (melhor tiro)" % distancia
    else:
        print "%.2f cm" % distancia

print "--"
print "num tiros: %d" % num_tiros
print "melhor tiro: %.2f cm" % melhor_tiro
print "distancia media: %.2f cm" % (soma_dist/num_tiros)
    