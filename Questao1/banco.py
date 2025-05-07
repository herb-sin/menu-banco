from agencia import Agencia

class Banco:
    def __init__(self, numero):
        self._numero = numero
        self._lista_agencias = []

    def cadastrar_agencia(self, numero):
        self._lista_agencias.append(Agencia(numero))

    def remover_agencia(self, numero):
        self._lista_agencias = [a for a in self._lista_agencias if a._numero != numero]

    def buscar_agencia(self, numero):
        for agencia in self._lista_agencias:
            if agencia._numero == numero:
                return agencia
        return None

    def transferir(self, num_agencia1, num_conta1, num_agencia2, num_conta2, valor):
        agencia1 = self.buscar_agencia(num_agencia1)
        agencia2 = self.buscar_agencia(num_agencia2)
        if agencia1 and agencia2:
            conta1 = agencia1.buscar_conta(num_conta1)
            conta2 = agencia2.buscar_conta(num_conta2)
            if conta1 and conta2 and conta1.get_saldo() >= valor:
                conta1.creditar(-valor)
                conta2.creditar(valor)

    def relatorio(self):
        saldo_total = sum(sum(c.get_saldo() for c in a._lista_contas) for a in self._lista_agencias)
        return f"Banco {self._numero}: Agências = {len(self._lista_agencias)}, Saldo Total = {saldo_total}"
