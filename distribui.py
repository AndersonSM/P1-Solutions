# coding: utf-8
# distribui_alunos
# Anderson Sales

def distribui_alunos(turma1, turma2, capacidade):
    novalista = [[],[]]
    menor = turma1
    maior = turma2
    if len(turma2) < len(turma1):
        menor = turma2
        maior = turma1
    
    for i in range(len(menor)):
        if i < capacidade/2.0:
            novalista[0].append(turma1[i])
        else:
            novalista[1].append(turma1[i])
        if i < capacidade/2:
            novalista[0].append(turma2[i])
        else:
            novalista[1].append(turma2[i])
    
    for i in range(len(menor),len(maior)):
        if len(novalista[0]) < capacidade:
            novalista[0].append(maior[i])
        else:
            novalista[1].append(maior[i])
        
    return novalista

print distribui_alunos([7,8,9,0],[1,2,3,4,5],8)