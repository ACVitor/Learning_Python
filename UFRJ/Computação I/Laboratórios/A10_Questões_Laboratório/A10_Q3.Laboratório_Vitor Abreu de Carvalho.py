#Vitor Abreu de Carvalho

#Questão 3

def busca(s,matriz):
    '''Esta função busca e retorna na matriz dada as informações dos funcionários
    que trabalham no setor também dado.
    list -> list'''
    funcionarios = len(matriz)
    info = len(matriz[0])
    f_do_setor = []
    for i in range(funcionarios):
        if matriz[i][2] == s:
            list.remove(matriz[i],s)
            list.append(f_do_setor, matriz[i])
    if f_do_setor == []:
        return ['Nenhum registro encontrado']
    else:
        return f_do_setor

def dados():
    #Criando a matriz
    lista = []
    matriz = []
    print('--------Informe os dados do funcionário--------')
    nome = input('Nome do funcionário: ')
    list.append(lista,nome)
    registro = input('Registro: ')
    list.append(lista,registro)
    setor = input('Setor em que o funcionário trabalha: ')
    list.append(lista,setor)
    tel = input('Telefone: ')
    list.append(lista,tel)
    return lista

def main():
    print('----------Info Funcionários do setor----------',
          'Nesta função você irá armazenar os dados de diferentes funcionários e por fim, irá buscar as informações daqueles que pertencem a determinado setor.\n', sep = '\n \n')
    info = int(input('Deseja adicionar um funcionário? Digite 1 se sim ou 2 se não: '))
    matriz = []
    if info == 1:
        while info == 1:
            list.append(matriz,dados())
            info = int(input('Deseja adicionar outro funcionário? Digite 1 se sim ou 2 se não: '))

        print('--------Busca--------')
        #Informar o setor como string
        s = input('Informe o setor para busca das informações dos funcionários: ')
    
        resultado = busca(s,matriz)
    
        for i in range(len(resultado)):
            print (resultado[i])
    else:
        print ('Sem registros')

main()
