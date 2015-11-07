# coding: utf-8
# proximo_media
# Anderson Sales

def proximo_da_media(lista):
    media = sum(lista)/len(lista)
    prox = lista[0]
    for e in lista:
        if abs(e-media) < abs(prox-media):
            prox = e
    return prox