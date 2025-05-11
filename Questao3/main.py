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
    print("14 - Somar Duas Contas")  # Nova opção
    print("15 - Somar Duas Agências")  # Nova opção
    print("16 - Sair")  # Opção "Somar Dois Bancos" removida


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
            print(agencia)  # Usando __str__
        else:
            print("Agência não encontrada!")

    elif opcao == "4":
        numero_agencia = int(input("Número da agência: "))
        agencia = banco.buscar_agencia(numero_agencia)
        if agencia:
            tipo = input(
                "Tipo de conta (corrente/poupanca/automatica): ")
            numero_conta = int(input("Número da conta: "))
            saldo_inicial = float(
                input("Saldo inicial (padrão é 0): ") or 0)
            try:
                agencia.criar_conta(tipo, numero_conta, saldo_inicial)
                print(
                    f"Conta {numero_conta} do tipo {tipo} cadastrada com saldo inicial de R${saldo_inicial:.2f} na agência {numero_agencia}."
                )
            except ValueError as e:
                print(e)
        else:
            print("Agência não encontrada!")

    elif opcao == "5":
        numero_agencia = int(input("Número da agência: "))
        agencia = banco.buscar_agencia(numero_agencia)
        if agencia:
            numero_conta = int(input("Número da conta: "))
            try:
                agencia.remover_conta(numero_conta)
                print(
                    f"Conta {numero_conta} removida da agência {numero_agencia}!")
            except ValueError as e:
                print(e)
        else:
            print("Agência não encontrada!")

    elif opcao == "6":
        numero_agencia = int(input("Número da agência: "))
        agencia = banco.buscar_agencia(numero_agencia)
        if agencia:
            numero_conta = int(input("Número da conta: "))
            conta = agencia.buscar_conta(numero_conta)
            if conta:
                print(conta)  # Usando __str__
            else:
                print("Conta não encontrada!")
        else:
            print("Agência não encontrada!")

    elif opcao == "7":
        numero_agencia = int(input("Número da agência: "))
        num_conta = int(input("Número da conta: "))
        valor = float(input("Valor: "))
        resultado = banco.creditar(numero_agencia, num_conta, valor)
        print(resultado)

    elif opcao == "8":
        numero_agencia = int(input("Número da agência: "))
        num_conta = int(input("Número da conta: "))
        valor = float(input("Valor: "))
        resultado = banco.debitar(numero_agencia, num_conta, valor)
        print(resultado)

    elif opcao == "9":
        num_agencia1 = int(input("Número da agência de origem: "))
        num_conta1 = int(input("Número da conta de origem: "))
        num_agencia2 = int(input("Número da agência de destino: "))
        num_conta2 = int(input("Número da conta de destino: "))
        valor = float(input("Valor a transferir: "))
        try:
            resultado = banco.transferir(
                num_agencia1, num_conta1, num_agencia2, num_conta2, valor)
            print(resultado)
        except ValueError as e:
            print(e)

    elif opcao == "10":
        num_agencia = int(input("Número da agência: "))
        num_conta = int(input("Número da conta poupança: "))
        taxa_juros = float(input("Taxa de juros: "))
        agencia = banco.buscar_agencia(num_agencia)
        if agencia:
            conta = agencia.buscar_conta(num_conta)
            if isinstance(conta, Poupanca):
                conta.render_juros(taxa_juros)
                print(conta)  # Usando __str__
            else:
                print("Conta não é do tipo Poupança!")
        else:
            print("Agência não encontrada!")

    elif opcao == "11":
        print(banco)  # Usando __str__

    elif opcao == "12":
        num_agencia = int(input("Número da agência: "))
        agencia = banco.buscar_agencia(num_agencia)
        if agencia:
            print(agencia)  # Usando __str__
        else:
            print("Agência não encontrada!")

    elif opcao == "13":
        num_agencia = int(input("Número da agência: "))
        num_conta = int(input("Número da conta: "))
        agencia = banco.buscar_agencia(num_agencia)
        if agencia:
            conta = agencia.buscar_conta(num_conta)
            if conta:
                print(conta)  # Usando __str__
            else:
                print("Conta não encontrada!")
        else:
            print("Agência não encontrada!")

    elif opcao == "14":  # Somar duas contas
        num_agencia = int(input("Número da agência: "))
        agencia = banco.buscar_agencia(num_agencia)
        if agencia:
            num_conta1 = int(input("Número da primeira conta: "))
            conta1 = agencia.buscar_conta(num_conta1)
            if conta1:
                num_conta2 = int(input("Número da segunda conta: "))
                conta2 = agencia.buscar_conta(num_conta2)
                if conta2:
                    try:
                        soma_saldos = conta1 + conta2
                        print(f"Soma dos saldos: R${soma_saldos:.2f}")
                    except TypeError as e:
                        print(e)
                else:
                    print("Segunda conta não encontrada!")
            else:
                print("Primeira conta não encontrada!")
        else:
            print("Agência não encontrada!")

    elif opcao == "15":  # Somar duas agências
        num_agencia1 = int(input("Número da primeira agência: "))
        agencia1 = banco.buscar_agencia(num_agencia1)
        if agencia1:
            num_agencia2 = int(input("Número da segunda agência: "))
            agencia2 = banco.buscar_agencia(num_agencia2)
            if agencia2:
                try:
                    soma_agencias = agencia1 + agencia2
                    print(f"Soma das agências: {soma_agencias}")
                except TypeError as e:
                    print(e)
            else:
                print("Segunda agência não encontrada!")
        else:
            print("Primeira agência não encontrada!")

    elif opcao == "16":  # Sair
        print("Saindo...")
        break

    else:
        print("Opção inválida!")