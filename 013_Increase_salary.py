def increase():
    '''This function calculate the 15% incease of salary, given a initial valor by the user'''
    sal = float(input('Enter with a current salary: $'))

    print('With a increase, the new salary is {:.2f}'.format(sal*115/100))

increase()