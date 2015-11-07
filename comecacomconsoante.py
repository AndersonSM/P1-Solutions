# coding: utf-8
# soma_inteiros_intervalo
# Anderson Sales

nome = raw_input()
qtd = 0

if nome[0] not in "aeiou*":
    qtd = 1
while nome != "***":
    nome = raw_input()
    if nome[0] not in "aeiou*":
        qtd += 1

print "Palavras: %d" % qtd