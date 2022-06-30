#Vitor Abreu de Carvalho

#Questão 1

def contagem (ite, elem):
    '''Esta função retorna a quantidade de vezes que o elemento aparece no dado iterável
Instruções: Insira um dado do tipo iterável (lista, str ou tupla) e o elemento
iterable(tuple, list or str), elemento(int float, complex, str,...)-> int'''
    conta = 0
    #Passando por cada elemento do iterável
    for item in ite:
        #Verificando se o item aparece ou não no iterável
        if item == elem:
            conta += 1
        else:
            conta = conta
    return conta

#Questão 2
    
def contagem_trecho(ite,elem,i1 = 0 ,i2 = -1):
    '''Esta função retorna a quantidade de vezes que o elemento aparece no trecho do dado
iterável de entrada
Instruções: Insira um dado do tipo iterável(list,str, tuple), o elemento e o intervalo do trecho.
iterable(tuple,list,str), qualquer tipo de dado(int, float, complex,str,...) -> int'''
    conta = 0
    #Novo iterável com os limites estipulados pelo usuário
    novo_ite = ite[i1:i2]
    for item in novo_ite:
        if item == elem:
            conta += 1
        else:
            conta = conta
    return conta

#Questão 3

def atualiza_mascara(palavra,lista,letra):
    '''Esta função percorre a palavra procurando a letra dada. Quando encontra, a 'máscara'
que cobria a posição da letra é removida aparecendo a letra na nova atualização, caso a letra
pertença a palavra
str, list, str -> str'''
    #Para eliminar as diferenças nas palavras digitadas pelo usuário
    palavra = str.lower(palavra)
    letra = str.lower(letra)
    i = 0
    #Percorrendo letra por letra da palavra
    for item in palavra:
        if item == letra:
            lista = lista[:i] + list(letra) + lista[i:]
        else:
            lista = lista
        i = i + 1
    return lista

#Questão 4

#(a)            

def soma_serie (n):
    '''Esta função calcula a soma da série até o termo fornecido pelo usuário
Instruções: forneça um int
int -> int'''
    #definindo até onde o vai a soma
    intervalo = range(n+1)
    soma = 0
    for item in intervalo:
        soma = soma + ((-1)**item)/((2*item)+1)
    return soma

#(b)

def erro_soma():
    '''Esta função calcula a série até o erro de 0,01 retornando o número de termos
usados para o alcançar
-> tuple'''
    conta = 0
    soma = 0
    import math
    pi = math.pi
    #Definindo enquanto irá funcionar, e absoluto pois o primeiro valor é 0
    while abs(soma-(pi/4)) > 0.01:
        soma = soma_serie(conta)
        conta += 1
    #Menos 1 no retorno de conta, pois ele está contando a primeira passagem
    return (soma,conta-1)
    

