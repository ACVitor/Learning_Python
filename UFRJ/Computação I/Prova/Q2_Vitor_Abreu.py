#Vitor Abreu de Carvalho
#DRE: 121077657
# turma EM2

#Questão_2
def voltas(r, d):
    '''Esta função calcula e retorna o número de voltas dadas por um atleta dados a distância percorrida
por ele e o raio da pista circular'''
    from math import pi
    perimetro = 2*pi*r
    voltas = d/perimetro
    return round(voltas,2)
