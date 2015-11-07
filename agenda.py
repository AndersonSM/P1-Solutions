# coding: utf-8
# - 1º P7
# Anderson Sales de Menezes / 113110007

nomes = []
telefones = []

def inserir(nomes, telefones):
    qtd = int(raw_input())
    for i in range(qtd):
        nome = raw_input()
        nomes.append(nome)
        telefone = raw_input()
        telefones.append(telefone)

def buscar(procurado, nomes, telefones):
    possui = False
    for i in range(len(nomes)):
        if procurado == nomes[i]:
            possui = True
            print "Nome: %s" % nomes[i]
            print "Fone: %s" % telefones[i]
            print "----------"
    if possui == False:
        print "Nome inexistente"
        print "----------"

def imprimir(nomes, telefones):
    for i in range(len(nomes)):
        print "Nome: %s" % nomes[i]
        print "Fone: %s" % telefones[i]
        print "----------"

    
while True:    
    entrada = raw_input()

    if entrada == "inserir":
        inserir(nomes, telefones)
        
    if entrada == "buscar":
        procurado = raw_input()
        buscar(procurado, nomes, telefones)
        
    if entrada == "imprimir":
        imprimir(nomes, telefones)
        
    if entrada == "finalizar": break