# coding: utf-8
# soma_inteiros_intervalo
# Anderson Sales

num1 = int(raw_input())
num2 = int(raw_input())
soma = 0
for i in range(num1,num2+1):
    soma += i

print "Soma: %d" % soma