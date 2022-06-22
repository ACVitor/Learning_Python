import random
def presentation_draw():
    '''This function draws the order of presentation of 4 students'''
    a1 = input('Enter with the student name: ')
    a2 = input('Enter with the student name: ')
    a3 = input('Enter with the student name: ')
    a4 = input('Enter with the student name: ')
    lista = [a1,a2,a3,a4]
    random.shuffle(lista)
    print('{:=^29}'.format(' Order of the draw '))
    print('1°: {}\n2°: {}\n3°: {}\n4°: {}'.format(lista[0],lista[1],lista[2],lista[3]))       #Este método embaralha a lista

presentation_draw()