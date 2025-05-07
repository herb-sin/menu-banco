from banco import Banco
from agencia import Agencia
from conta import Conta
from conta import Poupanca
from conta import Corrente
from conta import Automatica


def exibir_menu():
    print("\n===== MENU BANCO =====")
    print("1 - Cadastrar Agência")
    print("2 - Remover Agência")
    print("3 - Buscar Agência")
    print("4 - Cadastrar Conta")
    print("5 - Remover Conta")
    print("6 - Buscar Conta")
    print("7 - Creditar em Conta")
    print("8 - Debitar de Conta")
    print("9 - Transferir entre Contas")
    print("10 - Render Juros em Conta Poupança")
    print("11 - Exibir Relatório do Banco")
    print("12 - Exibir Relatório de Agência")
    print("13 - Exibir Relatório de Conta")
    print("14 - Sair")


# Criando o banco
banco = Banco(1)

while True:
    exibir_menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        numero_agencia = int(input("Número da agência: "))
        banco.cadastrar_agencia(numero_agencia)
        print(f"Agência {numero_agencia} cadastrada!")

    elif opcao == "2":
        numero_agencia = int(input("Número da agência: "))
        banco.remover_agencia(numero_agencia)
        print(f"Agência {numero_agencia} removida!")

    elif opcao == "3":
        numero_agencia = int(input("Número da agência: "))
        agencia = banco.buscar_agencia(numero_agencia)
        if agencia:
            print(f"Agência {numero_agencia} encontrada!")
        else:
            print("Agência não encontrada!")

# Adiciona tratamento de exceção

    elif opcao == "4":
        numero_agencia = int(input("Número da agência: "))
        agencia = banco.buscar_agencia(numero_agencia)
        if agencia:
            tipo = input(
                "Tipo de conta (corrente/poupanca/automatica): ").strip().lower()
            numero_conta = int(input("Número da conta: "))
            saldo_inicial = float(input("Saldo inicial (padrão é 0): ") or 0)
            try:
                nova_conta = agencia.criar_conta(
                    tipo, numero_conta, saldo_inicial)
                print(
                    f"Conta {numero_conta} do tipo {tipo} cadastrada com saldo inicial de R${saldo_inicial} na agência {numero_agencia}.")
            except ValueError as e:
                print(e)
        else:
            print("Agência não encontrada!")

    elif opcao == "5":
        numero_agencia = int(input("Número da agência: "))
        agencia = banco.buscar_agencia(numero_agencia)
        if agencia:
            numero_conta = int(input("Número da conta: "))
            agencia.remover_conta(numero_conta)
            print(f"Conta {numero_conta} removida!")
        else:
            print("Agência não encontrada!")

    elif opcao == "6":
        numero_agencia = int(input("Número da agência: "))
        agencia = banco.buscar_agencia(numero_agencia)
        if agencia:
            numero_conta = int(input("Número da conta: "))
            conta = agencia.buscar_conta(numero_conta)
            if conta:
                print(f"Conta {numero_conta} encontrada! Saldo: {conta.saldo}")
            else:
                print("Conta não encontrada!")
        else:
            print("Agência não encontrada!")

    elif opcao == "7":
        num_agencia = int(input("Número da agência: "))
        num_conta = int(input("Número da conta: "))
        valor = float(input("Valor a creditar: "))
        banco.creditar(num_agencia, num_conta, valor)
        # Após o crédito, busca a conta para obter o saldo atualizado
        agencia = banco.buscar_agencia(num_agencia)
        if agencia:
            conta = agencia.buscar_conta(num_conta)
            if conta:
                print(f"Saldo atual da conta {num_conta}: {conta.saldo}")
            else:
                print(
                    f"Conta {num_conta} não encontrada na agência {num_agencia}.")
        else:
            print(f"Agência {num_agencia} não encontrada.")
        print(
            f"Valor de {valor} creditado na conta {num_conta} da agência {num_agencia}.")

    elif opcao == "8":
        num_agencia = int(input("Número da agência: "))
        num_conta = int(input("Número da conta: "))
        valor = float(input("Valor a debitar: "))
        banco.debitar(num_agencia, num_conta, valor)
        agencia = banco.buscar_agencia(num_agencia)
        if agencia:
            conta = agencia.buscar_conta(num_conta)
            if conta:
                print(f"Saldo atual da conta {num_conta}: {conta.saldo}")
            else:
                print(
                    f"Conta {num_conta} não encontrada na agência {num_agencia}.")
        else:
            print(f"Agência {num_agencia} não encontrada.")
        print(
            f"Valor de {valor} debitado da conta {num_conta} da agência {num_agencia}.")

    elif opcao == "9":
        num_agencia_origem = int(input("Número da agência de origem: "))
        num_conta_origem = int(input("Número da conta origem: "))
        num_agencia_destino = int(input("Número da agência de destino: "))
        num_conta_destino = int(input("Número da conta destino: "))
        valor = float(input("Valor a transferir: "))
        banco.transferir(num_agencia_origem, num_conta_origem,
                         num_agencia_destino, num_conta_destino, valor)
        agencia_origem = banco.buscar_agencia(num_agencia_origem)
        agencia_destino = banco.buscar_agencia(num_agencia_destino)
        if agencia_origem and agencia_destino:
            conta_origem = agencia_origem.buscar_conta(num_conta_origem)
            conta_destino = agencia_destino.buscar_conta(num_conta_destino)
            if conta_origem and conta_destino:
                print(
                    f"Saldo atual da conta origem ({num_conta_origem}): {conta_origem.saldo}")
                print(
                    f"Saldo atual da conta destino ({num_conta_destino}): {conta_destino.saldo}")
            else:
                print("Conta(s) não encontrada(s)!")
        else:
            print("Agência(s) não encontrada(s)!")

    elif opcao == "10":
        num_agencia = int(input("Número da agência: "))
        num_conta = int(input("Número da conta poupança: "))
        taxa_juros = float(input("Taxa de juros: "))
        agencia = banco.buscar_agencia(num_agencia)
        if agencia:
            conta = agencia.buscar_conta(num_conta)
            if isinstance(conta, Poupanca):
                conta.render_juros(taxa_juros)
                print(f"Juros aplicados! Novo saldo: {conta.saldo}")
            else:
                print("Conta não é do tipo Poupança!")
        else:
            print("Agência não encontrada!")

    elif opcao == "11":
        print(banco.relatorio())

    elif opcao == "12":
        num_agencia = int(input("Número da agência: "))
        agencia = banco.buscar_agencia(num_agencia)
        if agencia:
            print(agencia.relatorio())
        else:
            print("Agência não encontrada!")

    elif opcao == "13":
        num_agencia = int(input("Número da agência: "))
        num_conta = int(input("Número da conta: "))
        agencia = banco.buscar_agencia(num_agencia)
        if agencia:
            conta = agencia.buscar_conta(num_conta)
            if conta:
                print(conta.relatorio())
            else:
                print("Conta não encontrada!")
        else:
            print("Agência não encontrada!")

    elif opcao == "14":
        print("Saindo do sistema bancário. Até logo!")
        break

    else:
        print("Opção inválida! Escolha um número entre 1 e 14.")
