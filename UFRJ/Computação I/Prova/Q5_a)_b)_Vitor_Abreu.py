#Vitor Abreu de Carvalho
#DRE: 121077657
# turma EM2

#Questão_5
#a)

def pegatelefone (lista, nome):
    '''Esta função retorna o telefone do funcionário, caso exista, contido em um lista de informações
fornecida pelo usuário.
list, str -> str or int'''
    for i in range(len(lista)):
        infos = lista[i]
        if infos['nome'] == nome:
            return infos['telefone']
    return -1

#b)

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
