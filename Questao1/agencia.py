from conta import Conta

class Agencia:
    def __init__(self, numero):
        self._numero = numero
        self._lista_contas = []

    def cadastrar_conta(self, numero, saldo=0):
        conta = Conta(numero, saldo)
        self._lista_contas.append(conta)

    def remover_conta(self, numero):
        self._lista_contas = [c for c in self._lista_contas if c.get_numero() != numero]

    def buscar_conta(self, numero):
        for conta in self._lista_contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def creditar(self, numero, valor):
        conta = self.buscar_conta(numero)
        if conta:
            conta.creditar(valor)

    def debitar(self, numero, valor):
        conta = self.buscar_conta(numero)
        if isinstance(conta, Corrente):
            conta.debitar(valor)

    def relatorio(self):
        saldo_total = sum(c.get_saldo() for c in self._lista_contas)
        return f"Agência {self._numero}: Contas = {len(self._lista_contas)}, Saldo Total = {saldo_total}"
