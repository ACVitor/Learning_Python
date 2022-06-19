def conversor():
    '''This function convert a valor given in metros for a valor in millimetres and centimetres'''
    n = float(input('Enter a valor in metros: '))

    print('This valor in centimetres is: {:.2f}'.format(n/100))
    print('This valor in millimetres is: {:.2f}'.format(n/1000))

conversor()