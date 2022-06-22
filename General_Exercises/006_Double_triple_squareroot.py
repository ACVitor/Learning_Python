def dts():
    '''This function calculate the double, triple and square root of any number given by the user'''
    n = int(input('Enter any number: '))

    print('Results of the operations')
    print('{:<15}{:>}'.format('Double: ', n*2))
    print('{:<15}{:>}'.format('Triple: ', n*3))
    print('{:<15}{:>.2f}'.format('Square root: ', n**(1/2)))

dts()