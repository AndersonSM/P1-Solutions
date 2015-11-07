# coding: utf-8
# lanchemaispedido
# Anderson Sales

def lanchemaispedido(pedidos):
    maior = None
    for e1 in pedidos:
        cont = 0
        for e2 in pedidos:
            if e1 == e2:
                cont += 1
        if cont > len(pedidos)/2.0:
            maior = e1
    return maior