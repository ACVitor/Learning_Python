import math
def part_int():
    '''This function shows a int part of the any number'''
    n = float(input('Enter with any number: '))
    print('Int part: {}'.format(math.floor(n)))

    #Other Solution
    #print('Int part: {}'.format(math.trunc(n)))

part_int()


#Teste with emoji
#import emoji
#print(emoji.emojize('Hello, :earth_americas:', language = 'alias'))