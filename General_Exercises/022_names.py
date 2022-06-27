def names():
    '''This function change the name given in the start of the program in several ways'''
    nome = input('Write your name: ').strip()
    print('''1) name in upper: {}
2) name in lower: {}
3) number of letters: {}
4) number of letterrs of the first name: {}'''.format(nome.upper(),nome.lower(),len(nome)-nome.count(' '),len(nome.split()[0])))

### Modo explicativo
    #print(nome.upper())                 #nome.upper -> Deixa todos os caracteres maiusculos
    #print(nome.lower())                 #nome.lower -> Deixa todos os caractéres em minúsculo
    #print(len(nome.strip()))            #nome.strip -> remove ' ' por default ou outro caractere escolhido do inicio e do final da str
    #print(len(nome.split()))            #nome.split() -> Transfomar o texto em uma lista de palavras, cortando em ' ' por default

names()