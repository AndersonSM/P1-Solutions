# coding: utf-8
# soma_valores
# Anderson Sales

num = int(raw_input("valor? "))
qtd = 0
soma = 0.0
media = 0.0

if num > 0:
    qtd += 1
    soma += num
while num >= 0:
    num = int(raw_input("valor? "))
    if num >= 0:
        qtd += 1
        soma += num
if qtd != 0:
    media = float(soma)/qtd
    
print "Quantidade de valores: %d" % qtd
print "Soma dos valores: %.1f" % soma
print "Média: %.1f" % media