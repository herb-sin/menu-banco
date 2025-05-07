class Conta:
    def __init__(self, numero, saldo=0):
        self._numero = numero
        self._saldo = saldo

    def creditar(self, valor):
        self._saldo += valor

    def get_saldo(self):
        return self._saldo

    def get_numero(self):
        return self._numero

    def relatorio(self):
        return f"Conta {self._numero}: Saldo = {self._saldo}"
    
class Corrente(Conta):
    def __init__(self, taxa, numero, saldo=0):
        super().__init__(numero, saldo)
        self._taxa = taxa

    def debitar(self, valor):
        desconto = valor * self._taxa
        if self._saldo >= (valor + desconto):
            self._saldo -= (valor + desconto)
            return True
        return False
    
class Poupanca(Conta):
    def render_juros(self, taxa):
        self._saldo += self._saldo * taxa

class Automatica(Conta):
    _contador = 1

    def __init__(self, saldo=0):
        super().__init__(Automatica._contador, saldo)
        self._numero = Automatica._contador
        Automatica._contador += 1