def welcome():
    '''This function comes to welcome to the user of the program'''
    name = input("What is your name? ")
    print('Welcome,{}! \nPleased to meet you.\n'.format(name))

    #Exemplos de como organizar a impressão
    print('Welcome,{}! \nPleased to meet you.\n'.format(name))          #\n Pula para a linha seguinte
    print('Welcome,{:20}! \nPleased to meet you.\n'.format(name))       #{:20} name é escrito no espaço de 20 caracteres
    print('Welcome,{:>20}! \nPleased to meet you.\n'.format(name))      #{:>20} name é escrito no espaço de 20 caracteres e alinha à direita
    print('Welcome,{:^20}! \nPleased to meet you.\n'.format(name))      #{:^20} name é escrito no espaço de 20 caracteres e centralizado
    print('Welcome,{:=^20}! \nPleased to meet you.\n'.format(name))     #{:=^20} name é escrito no espaço de 20 caracteres, centralizado e com o simbolo = envolta
    print('Welcome,{}! \nPleased to meet you.'.format(name),end='')     #end='' Não bota o print seguinte na linha debaixo, pode colocar algum caractere dentro de ''
    print('--------')
welcome()