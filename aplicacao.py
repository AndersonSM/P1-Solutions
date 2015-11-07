# coding utf-8
# aplicacao_polinomios
# Anderson Sales

def calcula(lista, valor):
    soma = 0
    for i in range(len(lista)):
        soma += int(lista[i]) * valor**i
    print soma

while True:
    entrada = raw_input()
    if entrada == "fim":
        break
    if entrada[0] == "p":
        lista = entrada.split()[1:]
        print "novo polinomio"
    else:
        calcula(lista,int(entrada))