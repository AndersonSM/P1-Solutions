# coding: utf-8
# media_palavras
# Anderson Sales

palavra = raw_input()
total = float(len(palavra))
qtd = 1
while palavra != "fim":
    palavra = raw_input()
    if palavra != "fim":
        total += len(palavra)
        qtd += 1

if qtd == 1:
    print "0.0"
else:
    print "%.1f" % (total/qtd)