#Vitor Abreu de Carvalho

#Questão 1

def dados():
    '''Esta função retorna o número de vezes que dois dados precisaram ser jogados
até darem o mesmo valor.
Instruções: Como f(x) é  aleatória, apenas execute a função sem entrada.
nehnuma entrada -> int'''
    #Definindo os dados e a contagem
    from random import randint
    d1 = randint(1,6)
    d2 = randint(1,6)
    contador = 1
    #Definindo argumento de jogadas
    if d1!=d2:
        while d1!=d2:
            d1 = randint(1,6)
            d2 = randint(1,6)
            contador = contador + 1
        return contador
    else:
        return contador

#Questão 2

def contatinhos_app(lista,busca):
    '''Esta função procura e retorna as informações de um contato dada uma lista de
contatos como entrada.
Instruções: Forneça os dados de entrada como lista de listas e um str, segue o exemplo:
([['nome',[telefones],'e-mail','instagram'],['nome',[telefones],'e-mail','instagram'],...],busca)
list, str -> list'''
    #Descobrindo o número de contatos da lista e repetindo
    contador = 0
    nova_lista = []
    while contador < len(lista):
        #Verificando se o nome procurado está na lista fornecida
        if str.lower(busca) in str.lower(lista[contador][0]):
            nova_lista = nova_lista + [lista[contador],]
        else:
            nova_lista = nova_lista
        contador = contador + 1
    return nova_lista
