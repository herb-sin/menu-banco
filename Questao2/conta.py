# conta.py
class Conta:
    def __init__(self, numero, saldo=0.0):  # Garantir que saldo seja float desde o início
        self._numero = numero
        self._saldo = float(saldo)

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0 and abs(valor) > self._saldo:
            raise ValueError("Saldo insuficiente para realizar o débito.")
        self._saldo += valor

    @property
    def numero(self):
        return self._numero

    def relatorio(self):
        return f"Conta {self._numero}:\n- Saldo atual: R${self._saldo:.2f}"


class Corrente(Conta):
    def __init__(self, numero, taxa, saldo=0.0):
        super().__init__(numero, saldo)
        self.taxa = taxa

    def debitar(self, valor):
        valor_total = valor * (1 + self.taxa)
        if self.saldo >= valor_total:
            self.saldo -= valor_total  # Usar o setter
            return True
        return False


class Poupanca(Conta):
    def __init__(self, numero, saldo=0.0):
        super().__init__(numero, saldo)

    def render_juros(self, taxa):
        self.saldo *= (1 + taxa)  # Usar o setter


class Automatica(Conta):
    _contador = 1

    def __init__(self, saldo=0.0):
        super().__init__(Automatica._contador, saldo)
        Automatica._contador += 1
