from agencia import Agencia


class Banco:
    def __init__(self, numero):
        self._numero = numero
        self._lista_agencias = []

    def cadastrar_agencia(self, numero):
        self._lista_agencias.append(Agencia(numero))

    def remover_agencia(self, numero):
        self._lista_agencias = [
            a for a in self._lista_agencias if a.numero != numero]

    def buscar_agencia(self, numero):
        return next((agencia for agencia in self._lista_agencias if agencia.numero == numero), None)

    def transferir(self, num_agencia1, num_conta1, num_agencia2, num_conta2, valor):
        agencia1, agencia2 = self.buscar_agencia(
            num_agencia1), self.buscar_agencia(num_agencia2)

        if not agencia1 or not agencia2:
            raise ValueError("Uma das agências não foi encontrada.")

        conta1, conta2 = agencia1.buscar_conta(
            num_conta1), agencia2.buscar_conta(num_conta2)

        if not conta1 or not conta2:
            raise ValueError("Uma das contas não foi encontrada.")

        if conta1.saldo < valor:
            raise ValueError("Saldo insuficiente para transferência.")

        conta1.saldo = -valor  # Débito
        conta2.saldo = valor  # Crédito

        return f"Transferência de R${valor:.2f} realizada da conta {num_conta1} para {num_conta2}!"

    def relatorio(self):
        saldo_total = sum(
            sum(c.saldo for c in a._contas.values()) for a in self._lista_agencias
        )
        return f"Banco {self._numero}: Agências = {len(self._lista_agencias)}, Saldo Total = R${saldo_total:.2f}"

# usar o setter de saldo
    def creditar(self, num_agencia, num_conta, valor):
        agencia = self.buscar_agencia(num_agencia)
        if not agencia:
            return "Agência não encontrada!"

        conta = agencia.buscar_conta(num_conta)
        if not conta:
            return "Conta não encontrada!"

        conta.saldo = valor  # Usa o setter para creditar
        return f"Crédito de R${valor:.2f} realizado na conta {num_conta}!"

    def debitar(self, num_agencia, num_conta, valor):
        agencia = self.buscar_agencia(num_agencia)
        if not agencia:
            return "Agência não encontrada!"

        conta = agencia.buscar_conta(num_conta)
        if not conta:
            return "Conta não encontrada!"

        try:
            conta.saldo = -valor  # Usa o setter para debitar
            return f"Débito de R${valor:.2f} realizado na conta {num_conta}!"
        except ValueError as e:
            return str(e)  # Retorna a mensagem de erro
