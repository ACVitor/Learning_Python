def triangle_validity():
    '''This function checks the existence of the triangle'''
    r1 = float(input('Enter with a valor for the first line: '))
    r2 = float(input('Enter with a valor for the second line: '))
    r3 = float(input('Enter with a valor for the third line: '))

    if r1+r2 <= r3 or r1+r3 <= r2 or r3+r2 <= r1:
        print('This is a impossible triangle.')
    else:
        print('Yeah, this triangle is possible to exist.')

triangle_validity()