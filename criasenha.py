# coding: utf-8
# criasenha
# Anderson Sales

def criaSenhaFraca(palavra):
    senha = "((" + palavra + "))"
    return senha

def criaSenhaForte(palavra):
    palavra = criaSenhaFraca(palavra)[2:-2]
    senha = "(("
    for i in palavra:
        if i in "oO":
            senha += "0"
        elif i in "iILl":
            senha += "1"
        elif i in "eE":
            senha += "3"
        elif i in "oaA":
            senha += "4"
        elif i in "bB":
            senha += "6"
        elif i in "tT":
            senha += "8"
        else:
            senha += i
    senha += "))"
    return senha

while True:
    entrada = raw_input().split()
    if entrada == ["***"]: break
    palavra = entrada[0]
    tipo = entrada[1]
    if tipo == "fraco":
        print criaSenhaFraca(palavra)
    else:
        print criaSenhaForte(palavra)
