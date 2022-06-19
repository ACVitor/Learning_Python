def discount():
    '''This function calculate 5% discount upon a product'''
    valor = float(input('Enter with a valor of the product: $'))

    print('The valor with 5% discount is ${:.2f}'.format(valor-(valor*5/100)))
    #print('The valor with 5% discount is ${:.2f}'.format(valor * 95 / 100))

discount()