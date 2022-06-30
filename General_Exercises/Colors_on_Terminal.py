#Sentença padrão
    # \033[0;33;44m ... \033[m

#Significado
    # Estilo
        # 0 : None
        # 1 : Bold
        # 4 : Underline
        # 7 : Negative
    # Cor texto
        # 30 : White
        # 31 : Red
        # 32 : Green
        # 33 : Yellow
        # 34 : Blue
        # 35 : Purple
        # 36 : Cyan
        # 37 : Grey
    # Cor fundo
        # 40 : White
        # 41 : Red
        # 42 : Green
        # 43 : Yellow
        # 44 : Blue
        # 45 : Purple
        # 46 : Cyan
        # 47 : Grey

#Exemplos:

print('\033[1;32;45mTeste\033[m')
print('\033[1;36mTeste\033[m')
print('\033[2;;42mTeste\033[m')
print('\033[4;33mTeste\033[m')
print('\033[7;34;41mTeste\033[m')

#Sugestão:
#Criar dicionário para acessar as cores no código