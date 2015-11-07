# coding: utf-8
# tem123
# Anderson Sales

def tem123(lista):
    for i in range(len(lista)):
        if len(lista) >= 3:
            if i <= len(lista)-3:
                if lista[i] == 1 and lista[i+1] == 2 and lista[i+2] == 3:
                    return i
    return -1