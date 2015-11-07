# coding: utf-8
# soma_valores_positivos
# Anderson Sales

while True:
    num1 = int(raw_input("Número 1: "))
    if 100 >= num1 >= 0:
        soma = num1
        break
    else:
        print "Número 1 inválido. Por favor, digite novamente."
while True:
    num2 = int(raw_input("Número 2: "))
    if 100 >= num2 >= 0:
        soma += num2
        break
    else:
        print "Número 2 inválido. Por favor, digite novamente."
print "Soma: %d" % soma