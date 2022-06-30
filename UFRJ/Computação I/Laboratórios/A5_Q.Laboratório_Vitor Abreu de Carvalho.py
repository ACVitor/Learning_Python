#Vitor Abreu de Carvalho

#Teste com a função do app da questão 1 com lista

def c_app(L):
    '''Função que retorna uma lista com os dados de uma pessoa.
Informe os valores em no formato de lista do seguinte modo:
['nome',[tel_1,tel_2,...],'email','instagram']
lista -> lista'''
    L = L + ['Bruno Campos',['2199112233','2133992211'],'brunoc91@emailquente.com','@brunocampos91']
    return L

# Questão_1

#1_(a)

def contatinhosapp(nome, email, instagram, telefones=''):
    '''Função que retorna uma lista com os dados de uma pessoa.
Informe os valores no formato de lista do seguinte modo:
['nome','email','instagram',['tel_1','tel_2',...]]
lista -> lista'''
    t = telefones
# Obs.: t é a lista que contém todos os telefones que o usuário inreriu
    lista = [nome, t[0:1], email, instagram]
    return lista

#1_(b)

def atualizar_contato(nome,telefones, email, instagram, indice, info):
    '''Esta função atualiza uma informação específica de um contato
Informe os valores no formato de lista do seguinte modo:
['nome','email','instagram',['tel_1','tel_2',...], indice, 'info']
str, str, str, lista de str ou uma str, int, str -> lista'''
# Definição das listas  
    lista = [nome, telefones, email, instagram]
    i = [info]
# Mudança do dado
# Primeiro if é sobre a mudança das informações sem ser o telefone
    if indice == 0 or indice == 2 or indice == 3:
        lista = lista[0:indice] + i + lista[indice+1:]
        return lista
# Elif para a mudança do telefone indicando se o novo é igual ao antigo
    elif indice == 1 and telefones != info:
        lista = lista[0:indice] + i + lista[indice:]
        return lista
    else:
        return lista

# Questão_2

def amino(rna):
    '''Esta função identifica os aminoácidos presentes em uma dada molécula
de RNA com 9 caracteres
Instruções: Digite a molécula com até nove caracteres maiúsculos e entre aspas
exemplo: 'AAGUCUUUU'
str -> str'''
# Definição do dicionário de aminoácidos
    aminoacidos = {'UUU':'Phe' , 'CUU': 'Leu', 'UUA':'Leu', 'AAG':'Lisina',
                   'UCU':'Ser', 'UAU':'Tyr', 'CAA':'Gln'}
# Quebrando a str rna em blocos de 3 caracteres
    bloco1 = rna[0:3]
    bloco2 = rna[3:6]
    bloco3 = rna[6:]
# Indentificando o aminoácido
    return 'Você possuí os aminoácidos:' + str([aminoacidos[bloco1]] + [aminoacidos[bloco2]] + [aminoacidos[bloco3]])
# OBS.: retornei str para ficar mais interativo com o usuário
