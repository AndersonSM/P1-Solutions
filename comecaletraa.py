# coding: utf-8
# comeca_letra_a
# Anderson Sales

nome = raw_input()
qtd = 0

while nome[0] != 'A':
    nome = raw_input()
    qtd += 1

print "---"
print "%d %s" % (qtd, nome)