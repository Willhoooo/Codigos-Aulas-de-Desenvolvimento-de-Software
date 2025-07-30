# Início do programa de caixa eletrônico

def caixa_eletronico(saldo = 5000):

    print('Caixa Eletrônico da Maze Bank')

    saque = float(input('\nDigite o valor de saque: R$')) # Inserir valor de saque

    # Condições
    if saque <= saldo: # Se o valor de saque for menor ou igual à 5000, o saque é realizado
        total = saldo - saque

        print(f"\nSaque de R${saque} efetuado com sucesso!")
        print(f'Seu saldo restante é de: R${total}')

    else: # Se o valor de saque for maior que 5000, ele não realiza o saque
        print('Saldo insuficiente!')

# Chama a função
caixa_eletronico()

# Fim do programa