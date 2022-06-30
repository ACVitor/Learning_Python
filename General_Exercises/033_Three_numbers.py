def three_numbers():
    '''This function checks which is the larger number between three numbers'''
    n1 = float(input('Enter with the first number: '))
    n2 = float(input('Enter with the second number: '))
    n3 = float(input('Enter with the third number: '))
    # lista = [n1,n2,n3]
    # lista.sort()
    # print('The biggest number is {:.0f} and the smaller number is {:.0f}'.format(lista[2],lista[0]))

    ## Outro modo
    menor = n1
    if n2 < n1 and n2<n3:
        menor = n2
    elif n3 < n1 and n3 < n2:
        menor = n3

    maior = n1
    if n2 > n1 and n2 > n3:
        maior = n2
    elif n3 > n1 and n3 > n2:
        maior = n3

    print('The biggest number is {:.0f} and the smaller number is {:.0f}'.format(maior, menor))

three_numbers()