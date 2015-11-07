# coding: utf-8
# quantos_comeram
# Anderson Sales

def quantos_comeram(n_feijoadas, fila):
    total = 0
    for i in range(len(fila)):
        if fila[i]+total <= n_feijoadas:
            total += fila[i]
    return total