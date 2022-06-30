#Vitor Abreu de Carvalho

#Questão 2

#(i)
def area_trapezio(a,b,c):
    '''Esta função calcula a área de um trapézio.
int, int, int -> str'''
    area = (((a+b)*c)/2)
    r = str.format('A área de um trapézio de bases {0} e {1} e altura {2} é igual a: {3}', a, b, c, area)
    return r

#ii
def pxp(a,b,c):
    '''Esta função calcula o quadrado dos valores.
int, int, int -> str'''
    r1 = str.format('O quadrado de {} é igual a: {}', a, a*a)
    r2 = str.format('O quadrado de {} é igual a: {}', b, b*b)
    r3 = str.format('O quadrado de {} é igual a: {}', c, c*c)
    return (str.format('{0}\n{1}\n{2}',r1,r2,r3))

#iii
def media(a,b,c):
    '''Esta função calcula a média aritmética dos valores dados
int, int, int -> str'''
    m = ((a+b+c)/3)
    r = str.format('A média aritimética dos valores {0}, {1} e {2} é igual a: {3}', a, b, c, m)
    return r

#iv
def s_intervalo(a,b,c):
    '''Esta função calcula a soma do intervalo, com salto c, de a até b.
int,int,int -> str'''
    lista = list(range(a,b+1,c))
    soma = sum(lista)
    return (str.format('A soma do intervalo de {} à {} com saltos de {} é igual a: {} ',a ,b, c, soma))

def main():
    #Seleção da operação
    print('----------Operações-----------','[1] - Área do trapézio','[2] - Quadrado dos valores','[3] - Média aritmética',
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
    print (resultado)

main()
