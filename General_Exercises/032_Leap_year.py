from datetime import date
def leap_year():
    '''This function verify if the year is leap or not'''
    ano = int(input('Enter with any year or 0 for the current year: '))
    if ano == 0:
        ano = date.today().year
    if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
        print('{} is a leap year.'.format(ano))
    else:
        print('{} is not a leap year.'.format(ano))

leap_year()