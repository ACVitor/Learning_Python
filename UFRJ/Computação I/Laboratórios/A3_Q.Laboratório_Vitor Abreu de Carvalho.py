#Vitor Abreu de Carvalho

# Questão_1

def modulo (a):
    '''Função que calcula o módulo de um dado valor.
float -> float'''
#Aqui defini como float pois o conjunto dos racionais contém os inteiros,
# e nesta função podemos usar racionais também
# outra forma de denotar que pensei foi float or int -> float or int :)
    if a<0:
        return -a
    else:
        return a

# Questão_2

def delta(a,b,c):
    '''Esta função, dados os coeficientes a, b e c, calcula o discriminante de um
polinômio do segundo grau;
int, int, int -> int'''
    return b**2-4*a*c

def raizes(a,b,c):
    '''Função que calcula a quantidade de raízes de um polinõmio de segundo grau
dados os valores dos coeficientes.
int, int, int -> int'''
    if delta(a,b,c) > 0:
        return 'A função possuí duas raízes reais'
    elif delta(a,b,c) == 0:
        return 'A função possuí apenas uma raiz real'
    elif delta(a,b,c) < 0:
        return 'A função não possuí raiz real'

#Questão_3

def repetir(texto,n):
    '''Função que repete um dado número de vezes(n) um texto.
Instruções: Utilizar aspas ao inserir o texto. exemplo 'oi'
str, int -> str'''
    return texto*n

#Questão_4

def data(d,m,a):
    '''Função que dados o ano mês e dia, retorna estes valores organizados na
representação de data.
int, int, int -> str'''
#Nesta questão os números inteiros são uma representação e por isto foi feita a conversão
    return str(d)+'/'+str(m)+'/'+str(a)

#Questão_5

def f_comport (x):
    '''Função que determina o comportamento matemático do gráfico dado na questão 5.
float ->  float'''
#Aqui novamente defini como float pois o conjunto dos racionais contém os inteiros,
# e nesta função podemos usar racionais também
# outra forma de denotar que pensei foi float or int -> float or int :)
    if x<0:
        return 0
    elif x>=0 and x<2:
        return x
    elif x>=2 and x<=3.5:
        return 2
    elif x>3.5 and x<5:
        return 3
    elif x>=5:
        return x**2-10*x+28

#Questão_6
    
#6_(a)
    
def inss(sb):
    '''Função que determina e calcula o percentual de descontos do INSS a
a partir do salário bruto.
Instruções: Informe apenas o valor do salário bruto, sem o "R$" a frente.
float -> float'''
    if sb<=2000:
        return (6*sb)/100
    elif sb>2000 and sb<=3000:
        return (8*sb)/100
    elif sb>3000:
        return (10*sb)/100

#6_(b)

def i_renda (sb):
    '''Função que determina e calcula o percentual de descontos do imposto
de renda a partir do salário bruto.
Instruções: Informe apenas o valor do salário bruto, sem o "R$" a frente.
float -> float'''
    if sb<=2500:
        return (11*sb)/100
    elif sb>2500 and sb<=5000:
        return (15*sb)/100
    elif sb>5000:
        return (22*sb)/100

#6_(c)
    
def s_liquido(sb):
    '''Função que calcula e retorns o salário líquido a partir salário bruto.
Instruções: Informe apenas o valor do salário bruto, sem o "R$" a frente.
float -> float'''
    return sb - (inss(sb)+i_renda(sb))

#6_(c) Alternativa
#Pensei em retornar o salário como texto apenas para incluir o "R$"

def s_liquido_2(sb):
    '''Função que calcula e retorns o salário líquido a partir salário bruto.
Instruções: Informe apenas o valor do salário bruto, sem o "R$" a frente.
float -> str'''
    return 'R$'+str(sb - (inss(sb)+i_renda(sb)))
