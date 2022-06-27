def number_digits():
    '''This function shows digits of the number given by the user'''
    n = int(input('Enter with a any number between 0 and 9999: '))
    u = n//1 % 10
    d = n//10 % 10
    c = n//100 % 10
    m = n// 1000 % 10
    print('''Unity: {} 
Set of ten: {}
Hundreds: {}
Thousands: {}'''.format(u,d,c,m))

number_digits()
