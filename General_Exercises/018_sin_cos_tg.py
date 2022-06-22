import math
def sct():
    '''This function caculate the sine, cosine and tangent of the angle given by the user'''
    a = math.radians(float(input('Enter with any angle: ')))
    print('{:=^30}'.format(' Trigonometric Table '))
    print('Sin: {:.2f}\nCos: {:.2f}\nTan: {:.2f}'.format(math.sin(a),math.cos(a),math.tan(a)))

sct()