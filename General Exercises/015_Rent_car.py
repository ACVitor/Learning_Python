def rent_car():
    '''This function calculates the valor of the rent car, based on rental days and the rate per km run.'''
    d = int(input('Enter with a quantity days of rent: '))
    k = float(input('Enter with a quantity km run: '))
    rent_v = d*60 + 0.15*k

    print('The valor of the rent car is: ${:.2f}'.format(rent_v))

rent_car()