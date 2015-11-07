# coding: utf-8
# media_9999
# Anderson Sales

num = int(raw_input())
soma = 0.0
qtd = 1

if num != 9999:
    soma = num
while num != 9999:
    num = int(raw_input())
    if num != 9999:
        soma += num
        qtd += 1
media = soma/qtd

print "%.1f" % media