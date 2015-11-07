# coding: utf-8

lista_nomes = []

while True:
    ultimo_nome = raw_input()
    if ultimo_nome == "####": break
    lista_nomes.append(ultimo_nome)
    
    # ALGORITMO SELECTION SORT (peguei do wikipedia, nao sei se
    # ta igual ao que o professor deu)
    for i in range(len(lista_nomes)-1):
		mini = i
		for j in range(i+1,len(lista_nomes)):
			if(lista_nomes[j]<lista_nomes[mini]):
				mini=j
 
		lista_nomes[i], lista_nomes[mini] = lista_nomes[mini], lista_nomes[i]
    
    for i in lista_nomes:
        if i == ultimo_nome:
            print "* " + i
        else:
            print i
    print "----"