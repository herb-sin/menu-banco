from banco import Banco
from agencia import Agencia
from conta import Corrente, Poupanca, Automatica

# Criar um banco
banco = Banco(1)  # Adicionei um número ao banco

# Criar duas agências
agencia1 = Agencia(101)
agencia2 = Agencia(202)

# Adicionar as agências ao banco
banco.cadastrar_agencia(agencia1.numero)  # Usando o número da agência
banco.cadastrar_agencia(agencia2.numero)

# Criar contas para cada agência
def criar_contas(agencia):
    agencia.criar_conta("corrente", 1, 0.0)  # 1 Conta Corrente (taxa de 5%)
    agencia.criar_conta("poupanca", 2, 0.0)  # 2 Poupança
    agencia.criar_conta("poupanca", 3, 0.0)
    agencia.criar_conta("automatica", 4, 0.0)  # 3 Automática
    agencia.criar_conta("automatica", 5, 0.0)
    agencia.criar_conta("automatica", 6, 0.0)

# Criar contas nas duas agências
criar_contas(agencia1)
criar_contas(agencia2)

# Creditar 200.0 em todas as contas
for agencia in [agencia1, agencia2]:
    for numero in agencia._contas.keys():
        agencia.creditar(numero, 200.0)

# Debitar 100.0 de todas as contas
for agencia in [agencia1, agencia2]:
    for numero in agencia._contas.keys():
        agencia.debitar(numero, 100.0)

# Render juros de 5% em todas as contas de uma agência (exemplo: agência 1)
print("\nRelatório antes de aplicar juros na agência 101:")
print(agencia1)
print(agencia2)
for numero, conta in agencia1._contas.items():
    if isinstance(conta, Poupanca):  # Apenas contas que permitem juros
        conta.render_juros(0.05)

# Imprimir relatório após render juros
print("\nRelatório após aplicar juros na agência 101:")
print(agencia1)
print(banco)

# Remover uma conta de cada agência
if agencia1._contas:
    conta_para_remover_agencia1 = next(iter(agencia1._contas))
    agencia1.remover_conta(conta_para_remover_agencia1)
    print(f"\nConta {conta_para_remover_agencia1} removida da Agência {agencia1.numero}")

if agencia2._contas:
    conta_para_remover_agencia2 = next(iter(agencia2._contas))
    agencia2.remover_conta(conta_para_remover_agencia2)
    print(f"Conta {conta_para_remover_agencia2} removida da Agência {agencia2.numero}")


# Imprimir relatório após remover uma conta
print("\nRelatório após remover uma conta de cada agência:")
print(agencia1)
print(agencia2)
print(banco)

# Remover uma agência (exemplo: agência 2)
if banco._lista_agencias:
    agencia_para_remover = banco._lista_agencias[0].numero
    banco.remover_agencia(agencia_para_remover)

    # Imprimir relatório final
    print("\nRelatório final após remover a agência:")
    print(banco)
else:
    print("\nNão há agências para remover.")