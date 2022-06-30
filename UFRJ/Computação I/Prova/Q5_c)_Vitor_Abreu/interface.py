#Vitor Abreu de Carvalho
#DRE: 121077657
# turma EM2

#Questão_5

from servico import*

def formato():
    print("\nOlá, seja bem vindo ao programa.\n")    
    print("[1] Recolher o telefone de um funcionário.\n[2] Ajustar o salário de um funcionário.\n[3] Mostrar informações de um funcionário.\n[4] Motrar as informações de todos os funcionários.")
    a = int(input("\nPor favor informe a operação desejada: "))
    return a

def opera(lista,a):
    if a == 1:
        nome = input("Informe o nome completo do funcionário: ")
        resultado = pegatelefone(lista,nome)
        if resultado == -1:
            print ("Não foram encontrados funcionários com este nome")
        else:
            print (str.format("O telefone do funcionário {} é: {}",nome,resultado))
    elif a == 2:
        cpf = input("Informe o cpf do funcionário: ")
        valor = int(input("Informe o valor do novo salário: R$"))
        resultado = ajustasalario(lista,cpf,valor)
        if resultado == False:
            print("Não foram encontrados funcionários com este cpf")
        else:
            print(str.format("O salário do funcionário foi ajustado para R${}",valor))
    elif a == 3:
        nome = input("Informe o nome completo do funcionário: ")
        resultado = individuo(lista, nome)
        if resultado == False:
            print("Não foram encontrados funcionários com este nome")
        else:
            print(str.format("Nome:{} \nTelefone:{} \nCpf:{} \nIdade:{} \n", resultado['nome'],resultado['telefone'],resultado['cpf'],resultado['idade']))
    elif a == 4:
        resultado = plantel(lista)
    else:
        print("Valor de entrada inválido.")
