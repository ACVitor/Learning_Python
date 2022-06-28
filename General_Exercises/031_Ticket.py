def ticket():
    '''This function calculate the ticket price.'''
    d = float(input('Enter with a distance [km]: '))
    if d <= 200:
        passagem = 0.5*d
    else:
        passagem = 0.45*d
    print('The valor of the travel is: R${:.2f}'.format(passagem))

ticket()