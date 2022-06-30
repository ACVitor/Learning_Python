#Vitor Abreu de Carvalho
#DRE: 121077657
# turma EM2

#Questão_1
def compara (texto, n):
    '''Esta função compara o número de caracteres de um texto com um número, retornando
uma mensagem que indica qual dos dois é maior.
str, int -> str'''
    total_texto = len(texto)
    if total_texto > n:
        return 'Número fornecido menor que tamanho da string'
    elif total_texto < n:
        return 'Número fornecido maior que tamanho da string'
    else:
        return 'Número fornecido possui o mesmo tamanho da string'
