#Vitor Abreu de Carvalho
#DRE: 121077657
# turma EM2

#Questão_3
def media ():
    '''Esta função pede repetidamente um valor até que o usuário informe um número
negativo. Quando isto é feito, é calculado e informado na tela a média dos valores
informados.'''
    #Valor de entrada para iniciar a condição
    n = 0
    lista = []
    while n >= 0:
        n = int(input("Informe um valor: "))
        if n >= 0:
            list.append(lista,n)
    n = (sum(lista))/len(lista)
    print (str.format('A média dos números é: {0}',n))
