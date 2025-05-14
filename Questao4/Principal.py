from banco import Banco
from agencia import Agencia
from conta import Corrente, Poupanca, Automatica

# Criar um banco
banco = Banco(1)

# Criar duas agências
agencia1 = Agencia(101)
agencia2 = Agencia(202)

# Adicionar agências ao banco
banco.cadastrar_agencia(agencia1)
banco.cadastrar_agencia(agencia2)

# Função para criar contas conforme o enunciado
def criar_contas(agencia):
    agencia.criar_conta("corrente", 1, 0.0)  # Conta Corrente (taxa 1%)
    agencia.criar_conta("poupanca", 2, 0.0)  # Poupança
    agencia.criar_conta("automatica", 3, 0.0)  # Automática

# Criar contas nas agências
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

# Relatório inicial
print("\nRelatório inicial:")
print(agencia1)
print(agencia2)
print(banco)

# Render juros de 5% apenas nas contas Poupança da agência 101
print("\nAplicando juros de 5% nas contas Poupança da Agência 101...")
agencia1.aplicar_juros_poupanca(0.05)  # Método novo da classe Agencia

# Relatório após juros
print("\nRelatório após juros na Agência 101:")
print(agencia1)
print(agencia2)
print(banco)

# Remover 1 conta de cada agência (a primeira conta da lista)
print("\nRemovendo uma conta de cada agência...")
contas_agencia1 = list(agencia1._contas.keys())
contas_agencia2 = list(agencia2._contas.keys())
if contas_agencia1:
    agencia1.remover_conta(contas_agencia1[0])
if contas_agencia2:
    agencia2.remover_conta(contas_agencia2[0])

# Relatório após remoção de contas
print("\nRelatório após remoção de contas:")
print(agencia1)
print(agencia2)
print(banco)

# Remover 1 agência (a primeira da lista)
print("\nRemovendo a Agência 101...")
banco.remover_agencia(101)

# Relatório final
print("\nRelatório final:")
print(banco)