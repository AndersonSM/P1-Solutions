# coding: utf-8
# collatz_iteracoes
# Anderson Sales

num = int(raw_input())
qtd = 0

while num != 1:
    if num%2 == 0:
        num = num/2
    else:
        num = 3*num+1
    qtd += 1

print qtd