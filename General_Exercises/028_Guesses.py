from random import randint
def guesses():
    '''This function is a game where the user must guess which number is draw'''
    ns = randint(0,5)
    n = int(input('Enter with any number between 0 and 5: '))
    if ns == n:
        print('Congratulations! You are right.')
    else:
        print('Wrong answer, try again :(')

guesses()