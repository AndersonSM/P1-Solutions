# coding: utf-8
# mais_consoantes
# Anderson Sales

nome = raw_input()
vogal = 0
consoante = 0
qtd = 1

for i in nome:
    if i in "aeiou":
        vogal += 1
    else:
        consoante += 1
if consoante > vogal:
    print qtd
while consoante <= vogal:
    nome = raw_input()
    consoante = 0
    vogal = 0
    for i in nome:
        if i in "aeiou":
            vogal += 1
        else:
            consoante += 1
    qtd += 1

if qtd > 1:
    print qtd