#Vitor Abreu de Carvalho

#Questão 1

def matriz_x_n(matriz,n):
    '''Esta função calcula e retorna a matriz resultante da multiplicação
da matriz pelo número dados na chamada da função
list , int -> list'''
    #Contando o número de linhas e colunas
    linha = len(matriz)
    colunas = len(matriz[0])
    
    #Criando nova matriz
    m = []
    for i in range(linha):
        # lista esvazia na nova passagem para criar a linha nova
        l = []
        for j in range(colunas):
            # Criação da linha
            l = l + [0]
        #Colocando as linhas dentro da lista (formatando a nova matriz)
        list.append(m,l)

    #Executando a multiplicação
    for i in range(linha):
        for j in range(colunas):
            #Substituindo valores da multiplicação na nova matriz
            m[i][j]= matriz[i][j]*n
    return m


#Questão 2

def deu_match (dici):
    '''Esta função busca por casais que curtiram um ao outro em um dado
dicionário e retorna uma lista de tuplas com os casais.
dict -> list'''
    #Listando o nome das pessoas que estão no dicionário
    pessoas = list(dict.keys(dici))
    casais = []
    #Pegando pessoa por pessoa na lista de nomes
    for p in pessoas:
        #Atribuindo o valor da chave a variável likes
        #(Pegando a lista de curtidas da pessoa em questão)
        likes = dici[p]
        #Passando de pessoa em pessoa na lista da pessoa em questão
        for parceiro in likes:
            #Verificando se esta mesma pessoa está na lista de quem ela curtiu
            if p in dici[parceiro]:
                #Inserindo os casais em uma lista
                list.append(casais,(p,parceiro))
    #Tirando as repetições
    total_de_casais = int(len(casais)/2)
    encontrado = casais[:total_de_casais]
    return(encontrado)

#Questão 3

def quem_ligou(n,agenda):
    '''Esta função retorna as informações a pessoa que é proprietária do
numero(n) que ligou, dado o número da pessoa e a lista de seus contatos
Instruções: Insira o número de telefone como string e a agenda como uma lista de
lista com as informações
exemplo: ('21999999999',[['nome','telefone','gmail','instagram'],['Vitor','21999999999','vitor.com','vv']]
str + list -> list'''
    infos = []
    #Passando pelos contatos existentes na agenda
    for contato in agenda:
        #Verificando existência do telefone em algum contato na agenda (contato[1] para indexar onde está posicionado o telefone)
        if n in contato[1]:
            #Colocando as informações da pessoa que ligou numa lista para retorno
            list.append(infos,contato)
    return infos
