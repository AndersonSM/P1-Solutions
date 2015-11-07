# coding: utf-8
# herao
# Anderson Sales

num = float(raw_input())
iteracoes = 0
a = num/2
e = abs(a**2-num)

while e > 10**-4:
    a = (a + (num/a))/2
    e = abs(a**2-num)
    iteracoes += 1
raiz = a

print "%.2f %d" % (raiz, iteracoes)