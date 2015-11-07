# coding: utf-8
# conta_palavras
# Anderson Sales

def conta_palavras(k, palavras):
    total = 0
    lista = palavras.split(":")
    for i in lista:
        if len(i) >= k:
            total += 1
    return total