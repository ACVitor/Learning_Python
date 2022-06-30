#Vitor Abreu de Carvalho

#PASSO I: Criação da matriz

def cria_matriz():
    '''Esta função é responsável por criar a matriz'''
    import random
    #Criando uma matriz vazia
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            list.append(linha,0)
        list.append(matriz,linha)
        
    #Colocando os primeiros elementos
    for i in range(1,9):
        p = (random.sample([0,1,2,3],2))
        while matriz[p[0]][p[1]] != 0:
            p = (random.sample([0,1,2,3],2))
        matriz[p[0]][p[1]] = i
    
    #Completando os pares
    elementos = [1,2,3,4,5,6,7,8]
    for i in range(4):
        for j in range(4):
            if matriz [i][j] == 0:
                n = random.randint(0,len(elementos)-1)
                matriz[i][j] = elementos[n]
                list.remove(elementos, elementos[n])
    return matriz

