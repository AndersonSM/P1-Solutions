# coding: utf-8

lista_nomes = []
lista_notas = []

while True:
    nome = raw_input()
    if nome == "fim": break
    nota = float(raw_input())
    
    lista_nomes.append(nome)
    lista_notas.append(nota)
    
    # ALGORITMO SELECTION SORT (peguei do wikipedia, nao sei se
    # ta igual ao que o professor deu)
    for i in range(len(lista_nomes)-1):
        mini = i
        for j in range(i+1,len(lista_nomes)):
            if(lista_notas[j]<=lista_notas[mini]):
                mini=j
 
        lista_nomes[i], lista_nomes[mini] = lista_nomes[mini], lista_nomes[i]
        lista_notas[i], lista_notas[mini] = lista_notas[mini], lista_notas[i]
    
print "Ranking:\n"
for i in range(-1, -len(lista_nomes)-1, -1):
    print "%d. %s: %.1f" % (-i, lista_nomes[i], lista_notas[i])