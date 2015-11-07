# coding: utf-8
# elementos_quimicos
# Anderson Sales

elementos = {'H': 1, 'S': 32, 'O': 16, 'C': 12, 'Ca': 40, 'Na': 23, 'P': 31}

while True:
    entrada = raw_input().split()
    if entrada[0] == "fim": break
    soma = 0
    
    for i in range(len(entrada)):
        if i < len(entrada)-1 and entrada[i+1].isdigit() == False \
            and entrada[i].isdigit() == False:
            soma += elementos[entrada[i]]
        elif entrada[i].isdigit() == True:
            soma += elementos[entrada[i-1]] * int(entrada[i])
        elif i == len(entrada)-1 and entrada[i].isdigit() == False:
            soma += elementos[entrada[i]]

    print soma