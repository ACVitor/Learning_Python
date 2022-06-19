def succ_pred():
    '''This function informs the successor and prodecessor of an informed number'''
    n = int(input('Enter any number: '))
    print('The sucessor of {} is {}, and your predecessor is {}.'.format(n, n+1, n-1))

succ_pred()