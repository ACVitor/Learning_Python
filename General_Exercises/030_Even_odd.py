def even_odd():
    '''This function irform if a number is even or odd'''
    n = int(input('Enter with any number: ' ))
    if n%2 == 0:
        print('The number {} is even.'.format(n))
    else:
        print('The number {} is odd.'.format(n))

even_odd()