# coding: utf-8
# letras_alternadas
# Anderson Sales

def letras_alternadas(string):
    nova = ""
    for i in range(0,len(string),2):
        nova += string[i]
    return nova

qtd = int(raw_input())

for i in range(qtd):
    string = raw_input()
    print letras_alternadas(string)