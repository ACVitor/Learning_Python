def traffic_ticket():
    '''This function inform if a driver will be fined or not. If yes, the amount of the fine is reported'''
    v = int(input('Enter with a car speed [km/h]: '))
    if v > 80:
        multa = 7*(v-80)
        print('You were fined in R${:.2f}'.format(multa))
    else:
        print('The driver was not fined.')

traffic_ticket()