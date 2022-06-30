#Vitor Abreu de Carvalho

#Questão 1

def jogada (n):
    '''Esta função calcula o número de faces que foram repetidas dado o número de vezes
que um dado foi lançado.
Instruções: Informe o número de jogadas.
int -> int'''
    lista = []
    repetiram = []
    q_faces = 0
    contador = 0
    from random import randint
    #Guardando os resultados das jogadas em uma lista
    while contador < n:
        contador = contador + 1
        valor = randint(1,6)
        list.append(lista,valor)
        #Mostrando na tela os resultados da n jogadas do dado
        print (str.format('Resultado da {} jogada: {}', contador, valor))
    #Selecionando os elementos que foram repetidos
    for i in lista:
        a = list.count(lista,i)
        if a > 1:
            #Contando o número de faces repetidas
            if i not in repetiram:
                list.append(repetiram,i)
                q_faces = q_faces+1
    return q_faces

#Questão 2

#(i)
def area_trapezio(a,b,c):
    '''Esta função calcula a área de um trapézio.
int, int, int -> str'''
    area = int(((a+b)*c)/2)
    r = str.format('(({0}+{1})*{2})/2 = {3}', a, b, c, area)
    return r

#ii
def pxp(a,b,c):
    '''Esta função calcula o produto dos valores por eles mesmos.
int, int, int -> str'''
    r1 = str.format('{}*{}={}', a, a, a*a)
    r2 = str.format('{}*{}={}', b, b, b*b)
    r3 = str.format('{}*{}={}', c, c, c*c)
    return (r1,r2,r3)

#iii
def media(a,b,c):
    '''Esta função calcula a média aritmética dos valores dados
int, int, int -> str'''
    m = int((a+b+c)/3)
    r = str.format('({0}+{1}+{2})/3 = {3}', a, b, c, m)
    return r

#iv
def s_intervalo(a,b,c):
    '''Esta função calcula a soma do intervalo, com salto c, de a até b.
int,int,int -> str'''
    lista = list(range(a,b+1,c))
    soma = sum(lista)
    return soma

def main():
    #Seleção da operação
    print('[1] - Área do trapézio','[2] - Produto dos valores por eles mesmos','[3] - Média aritmética',
          '[4] - Soma do intervalo, com salto c, de a até b', sep ='\n')
    escolha = int(input('Digite o código da operação que deseja realizar: '))
    
    #Informando os valores de entrada
    a = int(input('Informe o valor de a: '))
    b = int(input('Informe o valor de b: '))
    c = int(input('Informe o valor de c: '))

    #Realizando a operação solicitada
    if escolha == 1:
        resultado = area_trapezio(a,b,c)
    elif escolha == 2:
        resultado = pxp(a,b,c)
    elif escolha == 3:
        resultado = media(a,b,c)
    elif escolha == 4:
        resultado = s_intervalo(a,b,c)
    return resultado

#Questão 3

def busca(s,matriz):
    '''Esta função busca e retorna na matriz dada as informações dos funcionários
    que trabalham no setor também dado.
    list -> list'''
    funcionarios = len(matriz)
    info = len(matriz[0])
    f_do_setor = []
    for i in range(funcionarios):
        if matriz[i][2] == s:
            list.remove(matriz[i],s)
            list.append(f_do_setor, matriz[i])
    if f_do_setor == []:
        return 'Nenhum registro encontrado'
    else:
        return f_do_setor

def dados():
    #Criando a matriz
    lista = []
    matriz = []
    print('--------Informe os dados do funcionário--------')
    nome = input('Nome do funcionário: ')
    list.append(lista,nome)
    registro = input('Registro: ')
    list.append(lista,registro)
    setor = input('Setor em que o funcionário trabalha: ')
    list.append(lista,setor)
    tel = input('Telefone: ')
    list.append(lista,tel)
    return lista

#################### Proposta de solução 1 (Questão 3) ####################

def main_1():
    print('[1]-Sim','[2]-Não')
    info = int(input('Deseja adicionar um funcionário? '))
    matriz = []
    if info == 1:
        while info == 1:
            list.append(matriz,dados())
            print('[1]-Sim','[2]-Não')
            info = int(input('Deseja adicionar outro funcionário? '))

        print('--------Busca--------')
        #Informar o setor como string
        s = input('Informe o setor para busca das informações dos funcionários: ')
    
        resultado = busca(s,matriz)
    
        for i in resultado:
            print (i[0],i[1],i[2])
    else:
        return 'Sem registros'
    
#################### Proposta de solução 2 (Questão 3) ####################

def main_2():
    #Criando a Matriz
    n = int(input('Quantos funcionários existem? '))
    contador = 0
    matriz = []
    
    if n > 0:
        while contador < n:
            list.append(matriz,dados())
            contador = contador +1

        print('--------Busca--------')
        #Informar o setor como string
        s = input('Informe o setor para busca das informações dos funcionários: ')

        resultado = busca(s,matriz)

        for i in resultado:
            print (i[0],i[1],i[2])
    else:
        return 'Sem registros'


    
    
    
        
