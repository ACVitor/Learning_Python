from random import choice           #Este método sorteia um elemento da lista
def chosen():
    '''This function chosen a student of the group with four'''
    a1 = input('Enter with the student name: ')
    a2 = input('Enter with the student name: ')
    a3 = input('Enter with the student name: ')
    a4 = input('Enter with the student name: ')
    lista = [a1,a2,a3,a4]
    print('The student {} was draw.'.format(choice(lista)))

chosen()