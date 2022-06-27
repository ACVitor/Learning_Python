def flname():
    '''This function prints the first and the last name of the complete name given by the user'''
    name = input('Enter with a complete name: ').strip()
    print('First name: {}\nLast name: {}'.format(name.split()[0],name.split()[-1]))

flname()