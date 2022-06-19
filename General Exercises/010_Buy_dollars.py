def buy_dollars():
    '''This function calculates how much dollars is possible to buy for a given amount in reals'''
    reais = float(input('Enter with an amount in reals: R$'))
    fc = 3.27

    print('With {:.2f}, is possible buy ${:.2f}'.format(reais,reais/fc))

buy_dollars()