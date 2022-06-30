#Vitor Abreu de Carvalho

# Questão_1

def siga(t):
    '''Esta função retorna a situação do aluno na disciplina dados seu nome,
suas três notas nas provas.
Instruções: Inserir o nome entre aspas.
tuple(str, int, int, int) -> tuple(string,float,string,string)'''
    nome = t[0]
    n1 = t[1]
    n2 = t[2]
    n3 = t[3]
    media = round(((n1+n2+n3)/3),1)
    s = ()
    
    if media >=7:
        s = ('aprovado.',' Parabéns!',)
        
    elif media<7 and media>=5:
        s = ('aprovado',)
        
    else:
        s = ('reprovado',)
        
    return (nome, media) + s

#Questão_2

def signo (ano):
    '''Esta função retorna o signo do zodíaco chinês dado o ano de nascimento
int -> str '''
    z = ('Macaco','Galo','Cão','Porco','Rato','Boi','Tigre','Coelho','Dragão','Serpente','Cavalo','Carneiro')
    identificador = ano%12
    return z[identificador]

#Questão_3

def tel (t):
    '''Esta função retorna o DDD e o número de telefone se válido, informado
o número na forma de str.
Instruções: Inserir o número entre aspas.
str -> tuple(str,str)'''
    k = len (t)
    if k == 8:
        return '', t
    elif k == 9:
        return '', t
    elif k == 10:
        return '(' + str(t[0:2]) + ')' + str(t[2:])
    elif k == 11:
        return '(' + str(t[0:2]) + ')' + str(t[2:])
    else:
        return '',''

#Questão_4

def f_data(data):
    '''Esta função retorna o possível formato em que a data foi inserida pelo usário.
Instruções: (i) digitar entre aspas
(ii) Informar os valores em 3 grupos de 2 algarismos separados por "/".
str -> tuple(str,str,str)'''
    d1 = int(data[0:2])
    d2 = int(data[3:5])
    d3 = int(data[6:])
    f = ()
    if 0<d1<=31 and 1<=d2<=12:
        f = ('dd/mm/yy',)
    if 0<d3<=31 and 1<=d2<=12:
        f = f + ('yy/mm/dd',)
    if 0<d1<=12 and 0<d2<=31:
        f = f + ('mm/dd/yy',)
    return f


    
