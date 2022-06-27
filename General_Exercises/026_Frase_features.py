def frase_features():
    '''This function prints the features of the frase given by the user.'''
    frase = input('Enter with any frase: ').strip()
    print('The letter a appears {} times.'.format(frase.lower().count('a')))
    print('The first position of the a is: {}°.'.format(frase.lower().find('a')+1))
    print('The last position of the a is: {}°.'.format(frase.lower().rfind('a')+1))

frase_features()