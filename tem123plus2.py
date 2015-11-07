# coding: utf-8
# tem123plus(2)
# Anderson Sales

def tem123plus(lista):
    pos1 = pos2 = pos3 = None
    for i in range(len(lista)):
        if lista[i] == 1:
            pos1 = i
            break
    print pos1
    for i in range(len(lista)):
        if lista[i] == 2 and i > pos1:
            pos2 = i
            break
    print pos2
    for i in range(len(lista)):
        if lista[i] == 3 and i > pos2:
            pos3 = i
    print pos3        
    if pos3 > pos2 > pos1 and pos1 != pos2 != pos3 != None:
        return pos1
    return -1