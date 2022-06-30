#Vitor Abreu de Carvalho

#PASSO 2: Interação

from A11_Passo1_Criacao_Matriz_Vitor_Abreu import cria_matriz

def m():
    #Criando a matriz de apresentação
    mascara = []
    for i in range(4):
        linha = []
        for j in range(4):
            list.append(linha,'*')
        list.append(mascara,linha)
    #Apresentando a máscara na tela
    #Reiniciando o jogo
    for i in range(4):
        print (str.format('{0} {1} {2} {3}',mascara[i][0],mascara[i][1],mascara[i][2],mascara[i][3]))
    return mascara

def apresentacao():
    '''Esta função organiza as informações na tela, visando a facilidade de
manipulação do programa.'''
    #Apresentação
    print ("---------- JOGO DA MEMÓRIA ----------\n")
    print ("Olá seja bem vindo ao game, abaixo você verá a tabela para a escolha da posição.\nAs posições variam de 0 à 3 para as linhas[x] e para as colunas[y]")
    print ("Para a escolha da posição digite como no exemplo a seguir\nExemplo: ")
    print ("Escolha a posição: [0,0]")
    print ("Divirta-se, e boa sorte!;)\n")

def interacao(matriz,mascara):

    #Variável de repetição do while
    continuar = 1
    k = 1
    
    while continuar == 1:
        if k>1:
            #Reiniciando o jogo
            for i in range(4):
                print (str.format('{0} {1} {2} {3}',mascara[i][0],mascara[i][1],mascara[i][2],mascara[i][3]))
        k = k +1
    
        #Verificando se o usuário acertou para continuar    
        z = 1
        while z == 1:
            
            escolha = validacao()
            #extraindo os elementos da entrada
            a = int(escolha[1])
            b = int(escolha[3])
            valor = matriz[a][b]

            #Apresentando o número escolhido
            mascara[a][b] = matriz[a][b]
            for i in range(4):
                print (str.format('{0} {1} {2} {3}',mascara[i][0],mascara[i][1],mascara[i][2],mascara[i][3]))

            escolha_2 = validacao()
            #extraindo os elementos da segunda entrada
            x = int(escolha_2[1])
            y = int(escolha_2[3])

            #Apresentando o segundo número escolhido
            mascara[x][y] = matriz[x][y]
            for i in range(4):
                print (str.format('{0} {1} {2} {3}',mascara[i][0],mascara[i][1],mascara[i][2],mascara[i][3]))

            #Verificação de acerto e erro
                
            if valor != mascara[x][y]:
                print ("Você errou... tente de novo.")
                z = 2
                mascara[a][b] = '*'
                mascara[x][y] = '*'

            #Verificando se o usuário ganhou
            elif valor == mascara[x][y]:
                g=0
                for i in range(4):
                    for j in range(4):
                        if mascara[i][j] != '*':
                            g = g+1
                if g==16:
                   print(str.format("Parabéns! Você conseguiu descobrir todas as casas"))
                   z = 2
            
                else:
                    print ("Parabéns! Você acertou, continue")
                    z = 1
        continuar = int(input("Quer tentar novamente? (Se sim digite 1, se não digite 2) "))
    print ("Fim de jogo, até a próxima!")

def validacao():
    c=1
    while c == 1:
        escolha = list(input("\nEscolha uma posição: "))
    #Verificação de validade da escolha
        x = int(escolha[1])
        y = int(escolha[3])

        if x<0 or x>3 or y<0 or y>3 or len(escolha)>5:
            print ('Posição inválida')
            c=1
        else:
            c=2
    return escolha

    
    
    
