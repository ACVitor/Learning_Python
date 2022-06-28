def leap_year():
    '''This function verify if the year is leap or not'''
    ano = int(input('Enter with any year: '))
    if ano%4 == 0:
        print('{} is a leap year.'.format(ano))
    else:
        print('{} is not a leap year.'.format(ano))

leap_year()