saldo = 0.0
opcao = ''
while opcao != 'Sair':
    opcao = input("\n\n\n\n\n\n\n\n\nSaldo: " + str(saldo) + "\n\nDigite uma opção:\n\n\tDepositar\n\tSacar\n\tSalvar\n\tCarregar\n\tSair\n")
    if opcao == 'Depositar':
        valor = float(input("Informe o valor a ser depositado: "))
        saldo += valor
    elif opcao == 'Sacar':
        valor = float(input("Informe o valor a ser sacado: "))
        if valor <= saldo:
            saldo -= valor
        else:
            print("\n\nQuer um cheque especial? Não tem saldo suficiente.\n")
            input()
    elif opcao == 'Salvar':
        salvar = open("saldo.lp1", "w")
        salvar.write(str(saldo))
        salvar.close()
    elif opcao == 'Carregar':
        carregar = open("saldo.lp1", "r")
        saldo = float(carregar.read())
        carregar.close()
