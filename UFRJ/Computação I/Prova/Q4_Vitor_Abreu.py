#Vitor Abreu de Carvalho
#DRE: 121077657
# turma EM2

#Questão_4
def media ():
    '''Esta função pede repetidamente um valor até que o usuário informe um número
negativo. Quando isto é feito, é calculado e informado na tela a média dos valores
informados.'''
    #Valor de entrada para iniciar a condição
    n = 0
    lista = []
    while n >= 0:
        n = float(input("Informe um valor: "))
        if n >= 0:
            list.append(lista,n)
    n = (sum(lista))/len(lista)
    print (str.format('A média dos números é: {0}',n))

def formato():
    '''Esta função modela a apresentação da função principal'''
    print ("Olá, seja bem vindo.\nIremos calcular a média dos valores que você inserir abaixo.")
    print ("Qualquer valor negativo quando inserido não será contabilizado na média e fechará o conjunto dos números que serão usados para o cálculo.\n")

def main():
    formato()
    #Executando a função media na chamada da principal
    media()
main()
