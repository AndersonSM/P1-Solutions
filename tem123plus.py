# coding: utf-8
# tem123plus
# Anderson Sales

def tem123plus(lista):
    pos1 = pos2 = pos3 = None
    for i3 in range(len(lista)):
        if pos2 == None:
            for i2 in range(len(lista)):
                if pos1 == None:
                    for i1 in range(len(lista)):
                        if lista[i1] == 1:
                            pos1 = i1
                            break
                if lista[i2] == 2 and i2 > pos1:
                    pos2 = i2
                    break
        if lista[i3] == 3 and i3 > pos2:
            pos3 = i3
    if pos3 > pos2 > pos1:
        return pos1
    return -1