# coding: utf-8
# inverte3a3
# Anderson Sales

def inverte3a3(string):
    nova = ""
    j = 0
    for i in range(1,(len(string)/3)+1):
        nova += string[-i*3:len(string)-3*j]
        j += 1
    return nova