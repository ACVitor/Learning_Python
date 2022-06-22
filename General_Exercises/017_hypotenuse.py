import math
def hypotenuse():
    '''This function calculates the hypotenuse of the rectangule triangle. Given the catheters by the user'''
    c1 = float(input('Enter with a valor of the first cathetus: '))
    c2 = float(input('Enter with a valor of the other cathetus: '))
    h = math.sqrt(c1**2 + c2**2)
    print('The hypotenuse length is {:.2}'.format(h))

hypotenuse()