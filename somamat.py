# coding: utf-8
# somamats
# Anderson Sales

def somamats(M1,M2):
    nova_matriz = []
    """for i in range(len(M1)):
        nova_matriz.append([])"""
    
    for i in range(len(M1)):
        nova_matriz.append([])
        for j in range(len(M1[0])):
            nova_matriz[i].append(M1[i][j]+M2[i][j])
    
    return nova_matriz