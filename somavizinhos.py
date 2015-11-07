# coding: utf-8
# soma_vizinhos
# Anderson Sales

def soma_vizinhos(matriz, lin, col):
    lin = lin-1
    col = col-1
    
    soma = matriz[lin][col]
    
    # somar elemento superior
    if lin-1 >= 0:
        soma += matriz[lin-1][col]
        
    # soma elemento inferior
    if lin+1 < len(matriz):
        soma += matriz[lin+1][col]
    
    # soma elemento do lado esquerdo
    if col-1 >= 0:
        soma += matriz[lin][col-1]
    
    #soma elemento do lado direito
    if col+1 < len(matriz[0]):
        soma += matriz[lin][col+1]
    
    return soma