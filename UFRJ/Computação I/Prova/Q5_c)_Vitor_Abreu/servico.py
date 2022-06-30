#Vitor Abreu de Carvalho
#DRE: 121077657
# turma EM2

#Questão_5
#Serviços

def pegatelefone (lista, nome):
    '''Esta função retorna o telefone do funcionário, caso exista, contido em um lista de informações
fornecida pelo usuário.
list, str -> str or int'''
    for i in range(len(lista)):
        infos = lista[i]
        if infos['nome'] == nome:
            return infos['telefone']
    return -1

def ajustasalario(lista,cpf,valor):
    '''Esta função ajusta o valor do salário de um determinado funcionário, caso exista, dados a lista contendo
as informações dos funcionários, o cpf do trabalhador em questão, e o novo valor de sua remuneração.
list, str, float -> bool'''
    for i in range(len(lista)):
        infos = lista[i]
        if infos['cpf'] == cpf:
            infos['salario'] = valor
            return True
    return False

def individuo(lista, nome):
    '''Esta função retorna as informações de um usuário dado seu nome.'''
    for i in range(len(lista)):
        infos = lista[i]
        if infos['nome'] == nome:
            return lista[i]
    return False

def plantel(lista):
    '''Função que formata as informações dos funcionários.'''
    for i in range(len(lista)):
        dados = list(dict.values(lista[i]))
        print(str.format("Nome:{} \nTelefone:{} \nCpf:{} \nIdade:{} \n", dados[0],dados[1],dados[2],dados[3]))
