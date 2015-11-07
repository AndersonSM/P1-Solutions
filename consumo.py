# coding: utf-8

listaCodigos = [] # lista pra armazenar o codigo dos consumidores
listaConsumo = [] # lista pra armazenar o consumo em kWh dos consumidores
listaValorConsumo = [] # lista pra armazenar o consumo em R$ dos consumidores
listaTipo = [] # lista pra armazenar o tipo dos consumidores

totalRegular = totalEspecial = totalCarente = 0 # variaveis que vou
                                                # usar pra ir somando o consumo
                                                # de kWh a cada iteração

qtdRegular = qtdEspecial = qtdCarente = 0       # variaveis que vou
                                                # usar pra ir somando a qtd
                                                # de consumidores a cada iteração

N = int(raw_input()) #numero de consumidores

for i in range(N): # pra cada N, vou pegar 3 informações
    codigoDoConsumidor = raw_input()
    qtdKwhConsumida = float(raw_input())
    tipoDeConsumidor = raw_input()
    
    if tipoDeConsumidor == "R":
        qtdRegular += 1
        totalRegular += qtdKwhConsumida
        listaValorConsumo.append(qtdKwhConsumida * 0.7)
        listaConsumo.append(qtdKwhConsumida)
        listaCodigos.append(codigoDoConsumidor)
        listaTipo.append("R")
    
    elif tipoDeConsumidor == "E":
        qtdEspecial += 1
        totalEspecial += qtdKwhConsumida
        listaValorConsumo.append(qtdKwhConsumida * 0.5)
        listaConsumo.append(qtdKwhConsumida)
        listaCodigos.append(codigoDoConsumidor)
        listaTipo.append("E")
        
    elif tipoDeConsumidor == "C":
        qtdCarente += 1
        totalCarente += qtdKwhConsumida
        listaValorConsumo.append(qtdKwhConsumida * 0.3)
        listaConsumo.append(qtdKwhConsumida)
        listaCodigos.append(codigoDoConsumidor)
        listaTipo.append("C")

mediaGeral = (totalRegular + totalEspecial + totalCarente) / (qtdRegular+qtdEspecial+qtdCarente)

print "Total do consumo (Consumidor Regular) : %.2f kWh" % totalRegular
print "Total do consumo (Consumidor Especial) : %.2f kWh" % totalEspecial
print "Total do consumo (Consumidor Carente) : %.2f kWh" % totalCarente
print "---"
print "Média de consumo (Consumidor Regular) : %.2f kWh" % (totalRegular/qtdRegular)
print "Média de consumo (Consumidor Especial) : %.2f kWh" % (totalEspecial/qtdEspecial)
print "Média de consumo (Consumidor Carente) : %.2f kWh" % (totalCarente/qtdCarente)
print "---"
print "Média geral de consumo: %.2f kWh" % mediaGeral
print "---"
print "Consumidores acima da média geral:"

# como os indices são equivalentes em todas as listas, eu posso fazer isso:
for i in range(len(listaValorConsumo)):
    if listaConsumo[i] > mediaGeral:
        print "(%s) %5.5s R$ %.2f" % (listaTipo[i], listaCodigos[i], listaValorConsumo[i])

print "---"