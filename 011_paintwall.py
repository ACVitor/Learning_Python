def paint_wall():
    '''This function calculates the ink quantity is necessary to paint a wall, given your
    width and height'''
    w = float(input('Enter the width of the wall in metros: '))
    h = float(input('Enter the height of the wall in metros: '))
    area = w*h

    print('Is necessary {:.2f} liters of paint to paint a wall with {:.2f} m²'.format(area/2,area))

paint_wall()