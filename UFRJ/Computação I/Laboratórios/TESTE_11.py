#Vitor Abreu de Carvalho

#PASSO 2: Interação

from A11_Passo1_Criacao_Matriz_Abreu import cria_matriz

def interacao():
    '''Esta função organiza as informações na tela, visando a facilidade de
manipulação do programa.'''
    #Apresentação
    print ("---------- JOGO DA MEMÓRIA ----------\n")
    print ("Olá seja bem vindo ao game, abaixo você verá a tabela para a escolha da posição.\nAs posições variam de 0 à 3 para as linhas[x] e para as colunas[y]")
    print ("Para a escolha da posição digite como no exemplo a seguir\nExemplo: ")
    print ("Escolha a posição: [0,0]")
    print ("Divirta-se, e boa sorte!;)\n")

def jogo(escolha, escolha_2)
    #Variável de repetição do while
    continuar = 1

    original = cria_matriz()

    while continuar == 1:
        
        #Criando a matriz de apresentação
        matriz = []
        for i in range(4):
            linha = []
            for j in range(4):
                list.append(linha,'*')
            list.append(matriz,linha)
        
        for i in range(4):
            print (str.format('{0}{1}{2}{3}',matriz[i][0],matriz[i][1],matriz[i][2],matriz[i][3]))
            
        #Verificando se o usuário acertou para continuar    
        a = 1
        while a == 1:
            #extraindo os elementos da entrada
            x = int(escolha[1])
            y = int(escolha[3])
            valor = original[x][y]

            #Apresentando o número escolhido
            matriz[x][y] = original[x][y]
            for i in range(4):
                print (str.format('{0}{1}{2}{3}',matriz[i][0],matriz[i][1],matriz[i][2],matriz[i][3]))

            escolha_2 = list(input("Escolha outra posição [x,y]: "))
            #extraindo os elementos da segunda entrada
            x = int(escolha_2[1])
            y = int(escolha_2[3])

            #Apresentando o segundo número escolhido
            matriz[x][y] = original[x][y]
            for i in range(4):
                print (str.format('{0}{1}{2}{3}',matriz[i][0],matriz[i][1],matriz[i][2],matriz[i][3]))

            #Verificação de acerto e erro
                
            if valor != matriz [x][y]:
                print ("Você errou... tente de novo.")
                a = 2
                continuar = int(input("Quer tentar novamente? (Se sim digite 1, se não digite 2) "))
            else:
                print ("Parabéns! Você acertou")
                a = 1
    print ("Fim de jogo, até a próxima!")
