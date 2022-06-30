#Vitor Abreu de Carvalho

#Questão 1

def repetiu_face (resultados):
    '''Esta função calcula o número de vezes que ocorreram repetições de faces depois do
dado ser lançado n vezes lançado.
Instruções: Informe o número de jogadas.
int -> int'''
    ocorrencias = []
    n = len(resultados)
    i = 0
    #Criando lista um lista de lista dos elementos que repetiram
    #Vazio caso não houver sequência
    for i in range(n-1):
            repetiu = []
            #Para ingressar na lista o termo deve ser igual ao sucessor mas diferente do antecessor para eliminar as repetições
            if resultados[i] == resultados[i+1] and resultados[i] != resultados[i-1]:
                list.append(repetiu,resultados[i])
                contador = 2
            else:
                repetiu = repetiu
            list.append(ocorrencias,repetiu)
            
    #Retirando a ocorrência de vazios
    vazios = list.count(ocorrencias,[])
    total = len(ocorrencias) - vazios
    return total

def main():
    '''Função principal que calcula o número de vezes que ocorreram repetições de faces depois do
dado ser lançado n vezes lançado.'''
    from random import randint
    print('---------- Face Repetida ----------\n \n Neste programa vamos calcular quantas vezes ocorreram repetições\n de uma mesma face depois do laçamento de um ou mais dados \n')
    faces = int(input('Indique o número de faces que seu dado possui: '))
    dados = int(input('Indique quantas vezes o dado será lançado: '))

    #Gerando a lista resultados que será aplicada na função repetiu_face
    resultados = []
    for i in range(dados):
        list.append(resultados,randint(1,faces))

    print (str.format('\nNas {0} vezes que o dado foi jogado, ocorreram {1} situações em que uma face foi repetida mais de uma vez. \n', dados, repetiu_face(resultados)))
    info = int(input('Deseja ver a lista de resultados? digite 1 se sim ou 2 caso não queira: '))
    if info == 1:
        print (str.format('{0}\n Fim do programa',resultados))
    elif info ==2:
        print ('Fim do programa')
main()
    
