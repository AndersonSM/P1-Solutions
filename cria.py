# coding: utf-8
# cria_login
# Anderson Sales

def cria_login(nome):
    nome = nome.split()
    login = nome[0].lower()
    for i in range(1,len(nome)):
        if nome[i] not in "dedoda":
            login += nome[i][0].lower()
    return login

while True:
    nome = raw_input()
    if nome == "fim": break
    else:
        print "%s: %s" % (nome, cria_login(nome))