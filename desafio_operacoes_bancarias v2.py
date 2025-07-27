#Menu de opções do Usuário
menu = """

Por gentileza, informar a operação desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
[S] Nova Conta
[N] Novo usuário
[L] Listar contas

=> """

#Variáveis e Constante
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []

#Função Deposito

def deposito(saldo, limite,extrato, /):

    if operacao_deposito < 0:
        print("Valores negativos não computados, tente novamente!")
    else:
        saldo = operacao_deposito + saldo
        extrato += f" Depósito: R$ {operacao_deposito:.2f}"
        print(f"O Valor de R$ {operacao_deposito:.2f}, foi depositado com sucesso! \nSeu saldo atual é de: R$ {saldo:.2f}")
        return saldo, extrato

#Função Saque

def saque(*, saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    
    numero_saques += 1
    valor_limite_saque = limite
    saldo-= operacao_saque
    extrato += f" Saque: R$ {operacao_saque:.2f}"


    if numero_saques > LIMITE_SAQUES:
        print(f"Limite de saque diário execido, tente novamente amanhã.\nO número de saques efetuado foram de {numero_saques - 1:}")

    elif valor_limite_saque < operacao_saque:
        print ("Limite de saque não pode ultrapassar R$ 500,00!")


    elif saldo < operacao_saque:
        print("Saldo Insuficiente!")
        
    else:
        print(f"O Valor informado de R$ {operacao_saque:.2f} foi sacado com sucesso.\nSeu saldo atual é de: R$ {saldo:.2f}")
        return saldo, extrato



#Função Extrato

def extrato_fim(saldo , / , *, extrato,):


    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")



#Função Sair do App

def saida():
    print("Obrigado por escolher nossas agência!")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print((linha))



#Função Erro

def entrada_errada():
    print("Opção incorreta, tente novamente!")


while True:

        opcao = input(menu)

#Operação deposito
        if opcao == "1":
            operacao_deposito = float(input("Informar o valor a ser depositado: "))
            saldo, extrato = deposito(saldo, limite, extrato)

#Operação saque
        elif opcao == "2":
            operacao_saque = float(input("Informar o valor a ser sacado: "))
            saldo, extrato = saque(saldo=saldo, limite=limite, extrato=extrato, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

#Operacao Extrato
        elif opcao == "3":
            extrato_fim(saldo, extrato=extrato)

#Operacao Sair
        elif opcao == "0":
            saida()

#Operacao Criar Cliente    
        elif opcao == "S":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "N":
            criar_usuario(usuarios)

        elif opcao == "L":
            listar_contas(contas)

#Operacao Erro
        else:
            entrada_errada()


