def increase():
    '''This function calculates the increase in wage'''
    s = float(input('Enter with a wage: R$ '))
    if s > 1250:
        a = s + s*10/100
    else:
        a = s + s*15/100
    print('The new wage with increase is R${}'.format(a))

increase()