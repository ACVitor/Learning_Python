def read():
    '''This function prints some informations for the given informed by the user'''
    d = input('Inform something:')
    print('This given belongs there: {}'.format(type(d)))

    #Métodos que dizem se o valor inserido possui ou não uma característica
    print(d.isalpha())      #É alfabético?
    print(d.isnumeric())    #É número?
    print(d.isupper())      #Esta em maiúscula?
    print(d.islower())      #Esta em minuscula?
    print(d.isalnum())      #É um alfanumérico?
    print(d.istitle())      #Esta capitalizada? (Maiuscula e minuscula na mesma str)
read()