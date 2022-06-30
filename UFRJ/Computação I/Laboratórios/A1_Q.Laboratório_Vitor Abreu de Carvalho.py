#Vitor Abreu de Carvalho_Engenharia Mecânica

#Questão I

def area(b,h):
    '''Esta função calcula e retorna o valor da área de um retângulo
    Intruções:
    - Informe o valor da base (b) e da altura (h) da figura'''
    return b*h

#Questão II

def a_superficie(a):
    '''Esta função calcula e retorna o valor da area da superfície de um cubo
    Instruções:
    - Informe o valor da aresta (a)'''
    return a*12

#Questão III

def a_anel(r1,r2):
    '''Esta função calcula e retorna o valor da área de uma coroa circular
    Instruções:
    - Informe o valor do raio maior (r1) e do raio menor (r2) respectivamente'''
    return (3.14*(r1**2))-(3.14*(r2**2))

#Questão IV

def media(x,y):
    '''Esta função calcula e retorna o valor da média aritmética entre dois números'''
    return (x+y)/2

#Questão V

def f2_ordenada(a,b,c,x):
    '''Esta função calcula e retorna o resultado "f(x)" de uma função do segundo grau
    Instruções:
    - Informe o valor de a, b, c e da variável x respectivamente'''
    return (a*(x**2))+(b*x)+c

#Questão VI

def m_ponderada(n1,n2,p1,p2):
    '''Esta função calcula e retorna o valor da média ponderada entre dois números
    Instruções:
    - Informe o valor dos dois números (n1 e n2) primeiro
    - Em seguida informe o valor dos pesos (p1 para n1 e p2 para n2)'''
    return (n1*p1+n2*p2)/(n1+n2)

#Questão VII

def erro_aprox(q,n):
    '''Esta função calcula o erro de aproximação entre a soma de um P.G. infinita e
    a soma dos n primeiros termos desta mesma P.G.
    Instruções:
    - Informe o valor da razão (q) da P.G.
    - Em seguida informe a quantidade (n) dos termos desejados'''
    return (1/(1-q))-((q**n)-1)/(q-1)

#Questão VIII

def gorjeta(x):
    '''Esta função calcula o valor da gorjeta do garçom em função do valor da conta(x)'''
    return x*0.15

#Questão IX

def gorjeta_lei(x,y):
    '''Esta função calcula o valor da gorjeta do garçom em função do valor da conta e da
    porcentagem definida por lei
    Instruções:
    - Informe o valor da conta (x) e em seguida a porcentagem
    - Para a porcentagem informe o valor na forma decimal (Ex.: Para 10% informe 0.1)'''
    return x*y

#Questão X

def saldo(si,m,j):
    '''Esta função calcula o saldo final de uma conta bancária decorrido certo tempo.
    Instruções:
    - Informe o saldo inicial (si), os meses decorridos (m) e a taxa de juros mensal
    respectivamente
    - Para a taxa (j) informe o valor na forma decimal (Ex.: Para 10% informe 0.1)'''
    return si*(1+j*m)

#Questão XI

def desvio(vc,l,vb):
    '''Esta função calcula e retorna o desvio que uma correntesa provoca na trajetória de
    um barco.
    Instruções:
    - Informe a velocidade da correntesa (vc em m/s), a largura do rio (l em m) e a
    velocidade do barco (vb em m/s) respectivamente.'''
    return vc*(l/vb)
