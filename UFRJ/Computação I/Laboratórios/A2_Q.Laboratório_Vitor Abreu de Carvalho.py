#Vitor Abreu de Carvalho_Engenharia Mecânica

#Considerei que os valores de entrada são números inteiros

#Questão 1

#1.(a)_Teste das funções max e min

#>>> max(3,2.8,3.9)
#3.9
#>>> min(7,2,4,1,0)
#0'''

#1.(b)

def media(n1,n2,n3):
    '''Esta função calcula e retorna a média aritmética de três números inteiros;
int, int, int -> float'''
    return (n1+n2+n3)/3

#1.(c)

def diferenca(n1,n2,n3):
    '''Esta função calcula e retorna a diferença entre o maior valor inserido e a média
destes mesmos valores;
    int, int, int -> float'''
    return max(n1,n2,n3) - media(n1,n2,n3)

#1.(d)

def menor_mais_media(n1,n2,n3):
    '''Esta função retorna, dados três números, a soma do menor deles com a média;
int, int, int -> float'''
    return min(n1,n2,n3) + media(n1,n2,n3)

#Questão 2

#2.(a)

def delta(a,b,c):
    '''Esta função, dados os coeficientes a, b e c, calcula o discriminante de um
polinômio do segundo grau;
int, int, int -> int'''
    return b**2-4*a*c

#2.(b)

def raiz_1(a,b,c):
    ''' Esta funcão calcula e retorna a primeira raiz real de uma equação do segundo
grau, dados seus coeficientes a, b e c;
int, int, int -> float'''
    from math import sqrt
    return (-b + sqrt(delta(a,b,c)))/(2*a)

#2.(c)

def raiz_2(a,b,c):
    ''' Esta funcão calcula e retorna a segunda raiz real de uma equação do segundo
grau, dados seus coeficientes a, b e c;
int, int, int -> float'''
    from math import sqrt
    return (-b - sqrt(delta(a,b,c)))/(2*a)

#Questão 3

#3.(a)_Estudo do problema

#3.(b)

def n_termos(a1,an,r):
    '''Esta função calcular o número de termos dados os valores inicial e final e a
razão de uma progressão aritmética;
int, int, int -> int'''
    return (an-a1+r)/r

#3.(c)

def soma_termos(a1,an,r):
    '''Esta fução calcula a soma dos termos de uma PA finita dados os valores inicial,
final e a razão;
int, int, int -> float'''
    return ((a1+an)*n_termos(a1,an,r))/2

#Questão 4

#4.(a)

def hipotenusa(c1,c2):
    '''Esta função calcula e retorna o valor da hipotenusa de um triângulo retângulo
dado o valos de seus catetos c1 e c2;
int, int -> float'''
    import math
    return math.sqrt(c1**2+c2**2)

#4.(b)

def d_pontos(x1,y1,x2,y2):
    '''Esta função calcula a distância entre dois pontos em um plano dada as coordenadas;
Insira as cordenadas na ordem: Ponto mais a direita no plano (abscissa(x1), ordenada(y1))
ponto mais a esquerda no plano (abscissa(x2), ordenada(y2));
int, int, int, int -> float'''
    return hipotenusa((x2-x1),(y2-y1))

#4.(c)

def t_perimetro(c1,c2):
    '''Esta função calcula e retorna o perímetro de um triângulo reto dados os catetos;
int, int -> float'''
    return c1+c2+hipotenusa(c1,c2)

#4.(d)

def somaq_sen_cos(a):
    '''Esta função calcula e retorna o valor da soma dos quadrados do seno e do cosseno
de um ângulo;
Insira o valor do ângulo em graus
int -> float'''
    import math
    return (math.sin(math.radians(a)))**2+(math.cos(math.radians(a)))**2

#4.(e)

def pi(x=3.14):
    '''Valor de pi'''
    return x
    
def p_circulo (r):
    '''Esta função calcula o comprimento de uma circunferência;
Insira o valor do ângulo em graus
int -> float'''
    return 2*pi()*r

#Questão 5

def a_parte_circ(r,a=360):
    '''Esta função calcula e retorna o valor da área de um setor circular dados raio(r) e
ângulo (a);
Insira o valor do ângulo (a) em graus;
int -> float'''
    import math
    return (r**2*math.radians(a))/2




