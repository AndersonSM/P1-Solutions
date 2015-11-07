# coding: utf-8
# lista_presenca
# Anderson Sales

def cria_lista_presenca(turmas, nomes, turma):
    lista_presenca = []
    for i in range(len(turmas)):
        if turmas[i] == turma:
            lista_presenca.append(nomes[i])
    return lista_presenca
    
turmas = [1, 2, 2, 4, 5, 3, 5]
nomes = ["Maria", "Pedro", "Carlos", "Ana", "Carla", "Joao", "Jose"]
assert cria_lista_presenca(turmas, nomes, 5) == ["Carla", "Jose"]