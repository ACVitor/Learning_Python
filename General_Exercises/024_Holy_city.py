def holy_city():
    '''This function checks if a name of city contains santa in your beginning'''
    c = input('Enter with your city name: ').strip()
    print('santa' == c.lower().split()[0])

    ## Outra forma
    #print('santa'== c.lower()[:5])

holy_city()