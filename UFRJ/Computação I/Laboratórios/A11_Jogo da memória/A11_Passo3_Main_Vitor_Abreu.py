#Vitor Abreu de Carvalho

#PASSO 3: Interação

from A11_Passo1_Criacao_Matriz_Vitor_Abreu import cria_matriz
from A11_Passo2_Interacao_Vitor_Abreu import *

def main():
    '''Programa principal que executa as ações do jogo da memória'''
    
    #Criação da matriz aleatória
    matriz = cria_matriz()

    #Apresentação e armazenamento da máscara
    apresentacao()
    mascara = m()

    #Executando o jogo
    interacao(matriz,mascara)
    
main()
