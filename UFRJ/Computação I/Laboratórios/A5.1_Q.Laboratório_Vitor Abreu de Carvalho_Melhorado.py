#Vitor Abreu de Carvalho

# Questão_1

#Contatinhos_app, função do laboratório passado

def contatinhosapp(lista):
    '''Função que retorna uma lista com os dados de uma pessoa.
Informe os valores no formato de lista do seguinte modo:
['nome','email','instagram',['tel_1','tel_2',...]]'''
    nome = lista[0]
    email = lista[1]
    instagram = lista[2]
    telefones = lista[3]
# Obs.: t é a lista que contém todos os telefones que o usuário inreriu
    l = [nome, telefones[0], email, instagram]
    return l

#1_(b)

def atualizar_contato(lista, indice, info):
    '''Esta função atualiza uma informação específica de um contato
Informe os valores no formato de lista do seguinte modo:
['nome','tel','email','instagram', indice, 'info']
str, str, str, lista de str ou uma str, int, str -> lista'''
# Definição dos elementos da lista
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
