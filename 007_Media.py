def media():
    '''This function calculate media between two notes given by the student.'''
    n1 = float(input('Enter with your grade in the first test: '))
    n2 = float(input('Enter with your grade in the second test: '))

    media = (n1+n2)/2
    print('Your media in this period is {:.2f}'.format(media))

media()