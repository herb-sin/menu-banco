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

    def __add__(self, other):
        if isinstance(other, Conta):
            return self.saldo + other.saldo
        raise TypeError("Operação inválida: Soma apenas entre contas.")

    def __str__(self):
        return f"Conta: {self.numero}, Saldo: R${self.saldo:.2f}"


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

    def __str__(self):
        return f"Conta Corrente: {self.numero}, Saldo: R${self.saldo:.2f}, Taxa: {self.taxa*100} %"


class Poupanca(Conta):
    def __init__(self, numero, saldo=0.0):
        super().__init__(numero, saldo)

    def render_juros(self, taxa):
        self.saldo *= (1 + taxa)  # Usar o setter

    def __str__(self):
        return f"Conta Poupança: {self.numero}, Saldo: R${self.saldo:.2f}"


class Automatica(Conta):
    _contador = 1

    def __init__(self, saldo=0.0):
        super().__init__(Automatica._contador, saldo)
        self.numero = Automatica._contador  # Usar o setter
        Automatica._contador += 1

    def __str__(self):
        return f"Conta Automática: {self.numero}, Saldo: R${self.saldo:.2f}"