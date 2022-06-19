def sum_2():
    '''This function execute and prints the sum between two numbers provided by user'''
    n1 = int(input('Inform the first number: '))
    n2 = int(input('Inform the second number: '))
    s = n1+n2
    print('The sum between {} and {} is {}\n'.format(n1,n2, s))

    #Exemplos de como organizar a impressão
    print(('The sum between {} and {} is {:.2f}\n'.format(n1,n2, s)))     #{:.2f} Informa que queremos duas casas decimais
sum_2()
