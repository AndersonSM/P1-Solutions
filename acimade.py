# coding: utf-8
# acima_de
# Anderson Sales

def acima_de(N, L):
    novalista = []
    for i in range(len(L)):
        if L[i] > N:
            novalista.append(i)
    return novalista