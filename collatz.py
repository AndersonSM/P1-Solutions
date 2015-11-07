# coding: utf-8
# collatz
# Anderson Sales

num = int(raw_input())

print num
while num != 1:
    if num%2==0:
        num = num/2
    else:
        num = 3*num+1
    print num