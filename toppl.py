# coding: utf-8
# toppl - matrizes
# Anderson Sales

def filtra_alunos(alunos, inscritos, media):
    soma = 0
    for i in range(-len(alunos),0):
        if alunos[i][1] < media or alunos[i][0] not in inscritos:
            del alunos[i]
            soma += 1
    return soma