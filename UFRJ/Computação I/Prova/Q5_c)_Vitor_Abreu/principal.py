#Vitor Abreu de Carvalho
#DRE: 121077657
# turma EM2

#Importando os módulos
from servico import *
from interface import *

def main():
    '''Esta é a função principal que executa e chama os demais módulos.'''
    loop = 1
    while loop == 1:
        #Espaço para inserir a lista de dados dos funcionários
        lista = [{'nome': 'Vitoria Fernandes','telefone': '(21)32723053','cpf': '808.239.721-78','idade': 23},
                 {'nome': 'Breno Correia','telefone': '(14)99364107','cpf': '512.769.828-52','idade': 30},
                 {'nome': 'Amanda Gomes','telefone': '(11)43578751','cpf': '462.567.615-02','idade': 35},
                 {'nome': 'Vitor Abreu','telefone': '(21)971599832','cpf': '333.333.333-33','idade': 21}]

        #Solicitando as informações e operações ao usuário
        a = formato()
        #Executando a operação solicitada
        opera(lista,a)
        loop = int(input("Deseja reiniciar o programa([1]Sim [2] Não)? "))
    print("Fim do programa")
main()
    
