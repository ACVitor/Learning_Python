#Vitor Abreu de Carvalho

# Questão_1

def c_app_excluir(lista,telefone):
    '''Função que avalia se é verdade a remoção de um telefone de um contato
True: O telefone foi removido
False: O telefone não foi removido
Informe os valores no formato de lista do seguinte modo:
['nome',['tel_1','tel_2',...],'email','instagram']
lista, str -> bool'''
#Separando os dados da lista
    nome = lista[0]
    t = lista[1]
    email = lista[2]
    instagram = lista[3]
    l = []
#t é uma sublista com os telefones que o usuário inseriu
#Casos para exclusão do telefone
    if telefone in t:
        list.remove(t,telefone)
        l = [nome, t, email, instagram]
        return True
    else:
        l = [nome, t, email, instagram]
        return False

#Questão_2

def campeonato(tabela):
    '''Esta função avalia qual time obteve o maior número de pontos no campeonato,
retornando o nome dos times participantes, o número de pontos do campeão, e a média
de pontos do campeonato.
Instruções: Informe os dados no formato de dicionário como o exemplo:
{'time1':pontos(int), 'time2': pontos(int), ...}
dicionário -> lista'''
    times = list(dict.keys(tabela))
    pontos = list(dict.values(tabela))
#Transformando os pontos de cada time em uma lista ordenada
    list.sort(pontos)
    list.reverse(pontos)
#Escolha da maior pontuação
    winner = pontos[0]
#Cálculo da média de pontos do campeonato
    n = len (times)
    soma = sum(pontos)
    media = soma/n
    lista = times + [winner,media]
    return lista
    
