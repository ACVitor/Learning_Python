def temperature():
    '''This function convertes a temperature valor in °C (celsius) for °F (Fahrenheit) and °K(Kelvin)'''
    c = float(input('Enter with a temperature valor in °C: '))

    print('{:.2f} °C corresponds to {:.2f} °F and {:.2f} °K'.format(c, (9*c/5)+32, 273+c))

temperature()