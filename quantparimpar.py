# coding: utf-8
# quant_par_impar
# Anderson Sales

qtd_pares = 0
qtd_impares = 0
total_pares = 0
total_impares = 0

while True:
    num = int(raw_input())
    if num == 0: break
    if num % 2 == 0:
        qtd_pares += 1
        total_pares += num
    else:
        qtd_impares += 1
        total_impares += num
media_total = (total_impares + total_pares) / float(qtd_impares + qtd_pares)

print "pares: %d" % qtd_pares
print "impares: %d" % qtd_impares
if qtd_pares != 0:
    print "media pares: %.1f" % (float(total_pares)/qtd_pares)
if qtd_impares != 0:
    print "media impares: %.1f" % (float(total_impares)/qtd_impares)
print "media geral: %.1f" % (media_total)