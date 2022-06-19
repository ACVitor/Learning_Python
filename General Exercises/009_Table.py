def table():
    '''This function prints a table of the any number given by the user.'''
    n = float(input('Enter any number: '))

    c = 0
    while c<10:
        print('{:.0f} x {} = {:.0f}'.format(n,c,n*c))
        c += 1

table()