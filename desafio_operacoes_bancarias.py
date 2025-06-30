#Menu de opções do Usuário
menu = """

Por gentileza, informar a operação desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

#Variáveis e Constante
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

#Operação deposito

    if opcao == "1":
        operacao_deposito = float(input("Informar o valor a ser depositado: "))

        if operacao_deposito < 0:
            print("Valores negativos não computados, tente novamente!")
            break
        
        else:
            saldo = operacao_deposito + saldo
            extrato += f" Depósito: R$ {operacao_deposito:.2f}"
            print(f"O Valor de R$ {operacao_deposito:.2f}, foi depositado com sucesso! \nSeu saldo atual é de: R$ {saldo:.2f}")

#Operação saque

    elif opcao == "2":
        operacao_saque = float(input("Informar o valor a ser sacado: "))
        numero_saques += 1
        valor_limite_saque = limite
        saldo-= operacao_saque
        extrato += f" Saque: R$ {operacao_saque:.2f}"

        if numero_saques > LIMITE_SAQUES:
            print(f"Limite de saque diário execido, tente novamente amanhã.\nO número de saques efetuado foram de {numero_saques - 1:}")
            break

        if valor_limite_saque < operacao_saque:
            print ("Limite de saque não pode ultrapassar R$ 500,00!")
            break

        if saldo < operacao_saque:
            print("Saldo Insuficiente!")
            break

        else:
            
            print(f"O Valor informado de R$ {operacao_saque:.2f} foi sacado com sucesso.\nSeu saldo atual é de: R$ {saldo:.2f}")
        

#Operacao Extrato
    elif opcao == "3":
        
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")


#Operacao Sair
    elif opcao == "0":
        print("Obrigado por escolher nossas agência!")
        break

#Operacao Erro
    else:
        print("Opção incorreta, tente novamente!")
