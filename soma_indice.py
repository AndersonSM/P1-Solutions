# coding: utf-8
# soma_inteiros_intervalo
# Anderson Sales

num = int(raw_input())
lista = raw_input().split()
indice = -1

for i in range(0,len(lista)):
    if int(lista[i])+i == num:
        indice = i

print indice